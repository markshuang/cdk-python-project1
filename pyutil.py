import os
import boto3
import json
from botocore.exceptions import ClientError
from functools import lru_cache
import ldap3
#from ldap3 import Server, Connection, ALL
 
import cislib.config
from cislib.exceptions import AwsClientErrorException, LdapAuthenticationException
from cislib.logger import logger
from cislib.utility import log_milestone_inline


_ssm_client = boto3.client('ssm')

@lru_cache(maxsize=1)
def get_environment_value():
    return os.environ.get('ENV', 'dev')


@lru_cache(maxsize=256)
def get_ssm_parameter_by_name(name:str, withdecryption=False): 
    try:   
        return _ssm_client.get_parameter(Name=name,WithDecryption=withdecryption)["Parameter"]["Value"]
    except (ClientError) as client_error:
        raise  AwsClientErrorException('Calling aws ssm store failed - {0} with parameter - {1}'.format(client_error, name))

def get_ssm_parameter_by_env_app_name_no_exception(env:str, key:str, app:str, withDecryption = False):
    '''get_parameter would throw exception if parameter is not found.'''
    try:
       output = get_ssm_parameter_by_env_app_name(env, key, app, withDecryption)
    except:
       output = None
   
    return output      

def get_ssm_parameter_by_env_app_name(env:str, name:str, app:str= 'crload', withDecryption=False):
    ''' default for app is crload, otherwise, it uses what being passed, 
    like common, it uses pattern as '/ets/cis/{env}/{app}/{name}
    '''
    _ssm_key_template = '/ets/cis/%s/%s/%s'
    return get_ssm_parameter_by_name(_ssm_key_template % (env,app,name),withDecryption)

def put_ssm_parameter(type:str, name:str,value:str):
    _ssm_client.put_parameter(Type=type, Value=value, Name=name, Overwrite=True)

def get_parameters_by_path(path, with_decryption=True, recursive=True) -> dict:
    """ Return all of parameters' values under the hierarchy of that given path """
    items = {}

    def _parse_value(param_value, param_type):
        if param_type == 'StringList':
            return param_value.split(',')
        return param_value 

    def get_ssm_pages():
        ''' Small utility to implement pagination '''

        # boto3 paginators doc: http://boto3.readthedocs.io/en/latest/guide/paginators.html
        method = _ssm_client.get_paginator('get_parameters_by_path').paginate
       
        pages = method(
            Path=path,
            Recursive=recursive,
            WithDecryption=with_decryption          
        )

        return pages 

    for page in get_ssm_pages():
        for item in page['Parameters']:
            item['Value'] = _parse_value(item['Value'], item['Type'])
            items[item['Name']] = item['Value'] #item

    return items    

@lru_cache(maxsize=256)
def is_username_authenticated(user_name:str, password:str):

    if (user_name is None or len(user_name) == 0 or password is None or len(password)==0):
        error_message = 'User authentication failed, please check username or password.'
        ldap_errors =[]
        ldap_errors.append(error_message)
        ldap_errors.insert
        return False, ldap_errors

    env = get_environment_value()
    ldap_connection_string = get_ssm_parameter_by_env_app_name(env,'ldap.connection.string', 'common') 

    try:
        conn = ldap3.Connection(ldap_connection_string, user_name, password, auto_bind = True)    
        return True, None
    except Exception as ex:
        #TODO: log it first?
        error_message = 'User authentication failed with error - {}'.format(ex.__repr__())
        log_milestone_inline('LdapAuthentication','Failed', exception=LdapAuthenticationException(error_message))
        ldap_errors =[]
        ldap_errors.append(error_message)
        ldap_errors.insert
        return False, ldap_errors

def check_ssm_store_update():

    config_key = 'CRLoadConfigUpdateTime'
    env = get_environment_value()
    app = 'common'
    extra = {"custom_logging":{"ApplicationName":"CRLoad"}}
    if cislib.config._ssm_store_last_update_time is None:
        cislib.config._ssm_store_last_update_time = get_ssm_parameter_by_env_app_name(env, config_key, app)
        logger.info(f'ssm store - {config_key} is {cislib.config._ssm_store_last_update_time}', extra=extra)
        return
    
    current_value = _ssm_client.get_parameter(Name=f'/ets/cis/{env}/{app}/{config_key}', WithDecryption=False)["Parameter"]["Value"]
    if cislib.config._ssm_store_last_update_time != current_value:
        get_ssm_parameter_by_name.cache_clear()
        logger.info(f'clearing cache for ssm store.', extra=extra)
        cislib.config._ssm_store_last_update_time = current_value
        

-- decorator

import time
import json
import inspect
import traceback
import sys 
from string import Template 
from functools import wraps

from cislib.logger import logger
from cislib.exceptions import LogMileStoneException

def timethis(func):
    '''this logs only at the DEBUG level'''

    @wraps(func)
    def wrapper(*args, **kwargs):
       
        start  = time.perf_counter()  #time.process_time() #time.monotonic() #time.time()
        result = func(*args, **kwargs)
        end    = time.perf_counter()  #time.process_time() #time.monotonic() #time.time()
        
        template = Template('{"custom_logging":{"function":"${function}", "param":"${param}","time_took":"${time}"}}')

        #preprocess args

        log_message = template.substitute(function=func.__qualname__, param=preprocess_args(locals()),time="{0:.3f}".format(end-start))
        logger.debug("ExecutionDuration", extra=json.loads(log_message))
        return result
    return wrapper

def log_execution(function):
    '''this logs only at the DEBUG level'''

    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.debug('started execution of {}'.format(function.__qualname__))
        result = function(*args, **kwargs)
        logger.debug('done with execution of {}'.format(function.__qualname__))
        return result
    return wrapped    

def log_milestone(milestone:str):
    '''log the mile stone and its status '''


    def _log_milestone(function):
        @wraps(function)
        def wrapped(*args, **kwargs):

            milestone_name    = milestone
            milestone_message = '{{"custom_logging":{{"ApplicationName":"CRLoad","Milestone":"{}","MilestoneStatus":"{}"{}{}}}}}'
            duration_field    = ',"Duration":"{0:.3f}"'

            responsestatus_field = ',"MilestoneReponseStatusCode":"{}"' 

            #logger.info('LogMileStone',extra=json.loads(milestone_message.format(milestone_name,'Started', '')))
            start  = time.perf_counter()

            try:
                result   = function(*args, **kwargs)
                end      = time.perf_counter()
                duration = end - start 
            except:
                end      = time.perf_counter()
                duration = end - start

                logger.exception(sys.exc_info()[1], extra=json.loads(milestone_message.format(\
                    milestone_name,'Failed', duration_field.format(duration),'')))
                raise    

            #special case for end of event for CRLoadLambda
            if milestone == 'CRLoadLambda':
                status_code = result["statusCode"] 
                if status_code != 200:
                    logger.info('LogMileStone',extra=json.loads(milestone_message.format(\
                    milestone_name,'Failed', duration_field.format(duration),\
                        responsestatus_field.format(status_code))))
                else:
                    logger.info('LogMileStone',extra=json.loads(milestone_message.format(\
                    milestone_name,'Success', duration_field.format(duration),\
                        responsestatus_field.format(status_code))))      
            elif milestone in ['SchemaValidation','LdapAuthentication'] and result == False:
                    pass
                    #logger.error('LogMileStone',extra=json.loads(milestone_message.format(\
                    #milestone_name,'Failed', duration_field.format(duration),\
                    #    '')))
            else:    
                logger.info('LogMileStone',extra=json.loads(milestone_message.format(\
                    milestone_name,'Success', duration_field.format(duration),\
                        '')))

            return result

        return wrapped     
    
    return _log_milestone       

def preprocess_args(param:dict):
    '''this could get very complicated depending on type of parameter being passed, 
    and how many of them.
    For now, only dealing with following, can add more if needed.
    - string: 
    - dict: returns as 'dictionary' as it can contain anything that may cause issue for json
    - object: return object name
    '''
    if len(param['args']) == 0:
        return None

    args = param['args'][0]

    if isinstance(args, str):    
        return args
    if isinstance(args, dict):
        return 'dictionary...'
        #return str(args)    
    if isinstance(args, object):
        '''str(args) return <cislib.process_handler.OneProcess object at 0x0000014C9C1600A0>,
        so first split them, then take the first one on the list without first character.
        '''
        _list = str(args).split()
        return _list[0][1:]

-- util
import json 
from cislib.logger import logger

def get_aws_request_id(event, context):
    '''get aws_request_id from event or context'''
    
    try:
        aws_request_id = event['requestContext']['requestId']
    except (TypeError, KeyError):
        aws_request_id = getattr(context, 'aws_request_id', None)

    return aws_request_id    

def log_milestone_inline(milestone_name:str, milestone_status:str, \
    duration:float=0, exception:Exception=None, others:str=None):
    '''logging milestone at code level.
    others should be in key, value pairs - "key":"value","key1","value1"
    '''    

    duration_placeholder    = ''
    duration_field          = f',"Duration":"{duration:.3f}"'

    others_placerholder     = ''
    others_field            = f',{others}'

    if duration != 0:
        duration_placeholder = duration_field

    if others is not None:
        others_placerholder  = others_field     

    milestone_message = f'{{"custom_logging":{{"ApplicationName":"CRLoad","Milestone":"{milestone_name}",\
"MilestoneStatus":"{milestone_status}"{duration_placeholder}{others_placerholder}}}}}'
    
    if exception is not None:
        logger.exception(exception, extra=json.loads(milestone_message))

    return milestone_message

        
