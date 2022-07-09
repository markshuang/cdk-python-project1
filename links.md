07/09/2022  
-- Cloudfront, waf, api gateway  
https://www.wellarchitectedlabs.com/security/300_labs/300_multilayered_api_security_with_cognito_and_waf/  
-- build reusable components using service catalog in multi-account environment  
https://service-catalog-tools-workshop.com/  
https://awssecworkshops.com/  
https://www.vpcendpointworkshop.com/  
https://identity-round-robin.awssecworkshops.com/permission-boundaries-advanced/  
https://aws.amazon.com/blogs/security/get-more-out-of-service-control-policies-in-a-multi-account-environment/  
https://aws-samples.github.io/aws-iam-permissions-guardrails/  
https://aws.amazon.com/blogs/mt/codify-your-best-practices-using-service-control-policies-part-1/  
https://aws.amazon.com/blogs/mt/codify-your-best-practices-using-service-control-policies-part-2/  
https://summitroute.com/blog/2020/03/25/aws_scp_best_practices/  
https://asecure.cloud/l/scp/  
https://github.com/trussworks/terraform-aws-org-scp/blob/master/main.tf  
https://github.com/Snozzberries/AWS-SCPs  
https://aws-samples.github.io/aws-iam-permissions-guardrails/guardrails/scp-guardrails.html  
https://getstarted.awsworkshop.io/00-intro/05-required-knowledge.html  
https://getstarted.awsworkshop.io/01-up-front-tasks/01-review-requirements.html  
https://github.com/aws-samples/aws-get-started-workshop  
https://aws.amazon.com/solutions/implementations/serverless-transit-network-orchestrator/  

Why is a network-prod account being used for a development network? You may be asking why we’re creating a network-prod AWS account to contain a development network. Since the expectation is that the underlying development network for your teams should be treated as a production quality resource, the development network should reside in a production-oriented AWS account. Note that the actual development workloads will reside in team development accounts and not in the network-prod account. Only the underlying VPC and subnets reside in the network-prod account. Since a network-dev account would be positioned for your cloud foundation team to experiment and develop new networking capabilities, we would not want to put a production quality network in a network-dev account. Short of creating a dedicated, network-prod-common-dev account, this guide currently co-locates the centrally managed development VPC in the network-prod account. If you desire further isolation, then it’s recommended that you create a distinct account such as network-prod-common-dev to hold the centrally managed development network.  

https://getstarted.awsworkshop.io/03-dev/02-set-up-common-dev-network.html  
https://getstarted.awsworkshop.io/03-dev/03-set-up-team-dev-guardrails.html  

https://aws.amazon.com/solutions/implementations/aws-innovation-sandbox/  
https://docs.aws.amazon.com/solutions/latest/aws-innovation-sandbox/welcome.html  
https://github.com/awslabs/aws-innovation-sandbox  
https://aws.amazon.com/quickstart/terraform-modules/?quickstart-all.sort-by=item.additionalFields.sortDate&quickstart-all.sort-order=desc  
https://aws.amazon.com/solutions/implementations/aws-perspective/?did=sl_card&trk=sl_card  
https://aws.amazon.com/solutions/implementations/aws-firewall-mgr-automations-for-aws-orgs/?did=sl_card&trk=sl_card  
https://aws.amazon.com/solutions/implementations/centralized-logging/?did=sl_card&trk=sl_card  
https://aws.amazon.com/solutions/implementations/aws-devops-monitoring-dashboard/?did=sl_card&trk=sl_card  


-- typescript projects  
https://github.com/aws-samples/cdktf-aws-elb-cognito-auth  
https://github.com/aws-samples/cdktf-aws-elb-cognito-auth/blob/main/src/app.ts  
https://github.com/Pocket/terraform-modules/tree/main/src/pocket  
-- api gateway lambda dynamody, cognito  
https://github.com/hadock/CDKTF-From-Zero-To-Hero  
-- ec2 with nginx    
https://github.com/kksudo/devoops-cdktf/tree/main/ec2-nginx

---- Can look at the terraform modules (typescript) at pocket site, use them as models to create corresponding ones in python   
[terraform-modules/src/base at main · Pocket/terraform-modules (github.com) ](https://github.com/Pocket/terraform-modules/tree/main/src/base)   

-- search for cdktf python projects in Github  
[Search · cdktf (github.com) ](https://github.com/search?l=Python&p=3&q=cdktf&type=Repositories)  
--search for "Terraform cdk" in github  
[Search · "Terraform CDK" (github.com) ](https://github.com/search?l=Python&q=%22Terraform+CDK%22&type=Repositories)  

-- aws config  
[cdktf-ex/main.py at main · nbekenov/cdktf-ex (github.com)  ](https://github.com/nbekenov/cdktf-ex/blob/main/aws-config/main.py)  
[
cmclaughlin/hashiconf-cdktf-2021 (github.com)  ](https://github.com/cmclaughlin/hashiconf-cdktf-2021/)  

[Pocket/data-flows: Pocket data flows or chestrated using Prefect (github.com)  ](https://github.com/Pocket/data-flows)  

[cdktf/main.py at main · swethamothe/cdktf (github.com)  ](https://github.com/swethamothe/cdktf/blob/main/ec2/main.py)  

[cdktf/main.py at main · Devsharma27/cdktf (github.com)  ](https://github.com/Devsharma27/cdktf/blob/main/main.py)  

[cdktf-get-started/main.py at main · ibm-xaas/cdktf-get-started (github.com)](https://github.com/ibm-xaas/cdktf-get-started/blob/main/learn-cdktf-python/main.py)  

-- ecs, rds  
[cdktf-python/main.py at main · byhbt/cdktf-python (github.com)](https://github.com/byhbt/cdktf-python/blob/main/main.py)  

-- eks, helm with both aws provider and vpc, eks module   
[pavan8855/enthire: EKS using terraform-cdk (github.com)](https://github.com/pavan8855/enthire)  

-- vpc, lambda, api gateway  
[TerraformCdkNotesDemo/main.py at master · eladrapoportcybr/TerraformCdkNotesDemo (github.com)](https://github.com/eladrapoportcybr/TerraformCdkNotesDemo/blob/master/main.py)  

-- python invoke with ckdtf  
[vsuzdaltsev/terraform-cdk-examples: terraform-cdk (https://github.com/hashicorp/terraform-cdk) extended examples](https://github.com/vsuzdaltsev/terraform-cdk-examples)  

-- ecs  
[ContainersFromTheCouch-terraform-cdk-example/main.py at master · adamjkeller/ContainersFromTheCouch-terraform-cdk-example (github.com)](https://github.com/adamjkeller/ContainersFromTheCouch-terraform-cdk-example/blob/master/main.py)  

-- vpc, s3, rds, cache, ecr,  
[tomusher/wagtail-cloud: Terraform CDK constructs for deploying Wagtail to various cloud providers (github.com)](https://github.com/tomusher/wagtail-cloud)  

-- multi-stack v2  
[spareslant/oci_multi_stack_terraform_cdk_python_v2 (github.com)  ](https://github.com/spareslant/oci_multi_stack_terraform_cdk_python_v2)  

-- alb, ecs, rds, ssm, log  
[byhbt/cdktf-python: Project for exploring TFCDK (github.com) ](https://github.com/byhbt/cdktf-python)   

--vpc, subnet, internet gateway, route table, eks  
[cdktf-aws-python/main.py at main · celeguim/cdktf-aws-python (github.com)](https://github.com/celeguim/cdktf-aws-python/blob/main/cdktf-aws-python/main.py)  

-- using account, profile for different account and its profile for deployment  
[cdktf-ex/main.py at main · nbekenov/cdktf-ex (github.com)](https://github.com/nbekenov/cdktf-ex/blob/main/aws-config/main.py)  

-- static website on s3  
[cdktf-python-aws-staticwebsite/main.py at main · bjiusc/cdktf-python-aws-staticwebsite (github.com)](https://github.com/bjiusc/cdktf-python-aws-staticwebsite/blob/main/main.py)  

-- config and custom construct  
[cdktf-demo/main.py at main · caning01/cdktf-demo (github.com)](https://github.com/caning01/cdktf-demo/blob/main/main.py)  

{
  "language": "python",
  "app": "pipenv run python main.py",
  "projectId": "ea20d3f1-8b54-41f6-ab53-b4c4fcdd3ce9",
  "terraformProviders": ["aws@~> 4.4.0"],
  "terraformModules": [
    "terraform-aws-modules/vpc/aws@3.12.0",
    "terraform-aws-modules/s3-bucket/aws@2.14.0"
  ],
  "codeMakerOutput": "imports",
  "context": {
    "excludeStackIdFromLogicalIds": "true",
    "allowSepCharsInLogicalIds": "true"
  }
}

-- cross-stack, base-stack, lambda  
[cdktf-cross-stack/main.py at master · dhmistry3/cdktf-cross-stack (github.com)](https://github.com/dhmistry3/cdktf-cross-stack/blob/master/main.py)  

-- google  
[walkerk1980/cdktf_gcp_vm_unifi: terraform cdk stack to deploy Unifi controller on GCP (github.com)](https://github.com/walkerk1980/cdktf_gcp_vm_unifi)  

-- R53,  
[cdktf-boiler-template/main.py at main · gonzape27/cdktf-boiler-template (github.com)](https://github.com/gonzape27/cdktf-boiler-template/blob/main/main.py)  

-- codepipeline  
[cdktf-boiler-template/codepipeline.py at main · gonzape27/cdktf-boiler-template (github.com)](https://github.com/gonzape27/cdktf-boiler-template/blob/main/functions/codepipeline.py)  
-- codebuild, codepipeline,R53, cloudfront, certificate, iam  
[cdktf-boiler-template/functions at main · gonzape27/cdktf-boiler-template (github.com)](https://github.com/gonzape27/cdktf-boiler-template/tree/main/functions)  

-- vpc, subnet, ec2, instance profile  
[cdktf-samples-python/main.py at main · shazi7804/cdktf-samples-python (github.com)](https://github.com/shazi7804/cdktf-samples-python/blob/main/main.py)  

-- github repo  
[github-terraform-cdktf/main.py at develop · vishnu-chegondi/github-terraform-cdktf](https://github.com/vishnu-chegondi/github-terraform-cdktf/blob/develop/main.py)  

-- google  
[gcp-cdktf-example/main.py at main · lmayorga1980/gcp-cdktf-example (github.com)](https://github.com/lmayorga1980/gcp-cdktf-example/blob/main/gcp/main.py)  

-- serverless, S3, cloudfront, iam, lambda, dynamoDB, API gateway  
[Maed223/cdktf-integration-serverless-python-example: This repo contains an end to end example in Python for a serverless web application hosted on AWS and deployed with the CDK for Terraform. Please refer to the guide for more information. (github.com)](https://github.com/Maed223/cdktf-integration-serverless-python-example)  

-- ssm  
[tdd-terraform-cdk/main.py at master · yobooooi/tdd-terraform-cdk (github.com)](https://github.com/yobooooi/tdd-terraform-cdk/blob/master/main.py)  

--vpc, subnet, token  
https://github.com/chandler-mcfly/terraformAWSCdktfPython/blob/main/main_edited.py

-- api gateway, lambda, aws config, waf, aws firewall manager  
[nbekenov/cdktf-ex: Example of using Terraform CDK (github.com)](https://github.com/nbekenov/cdktf-ex)  

-- Developer's Helper to Docker, Kubernetes, and Terraform. Fully automatic, without any config or question  
[gepp/main.py at main · gurayops/gepp (github.com)](https://github.com/gurayops/gepp/blob/main/main.py)  

[Creating Kubernetes Cluster on Azure with Terraform and Python using CDK for Terraform | by Guray Yildirim | Medium](https://medium.com/@gurayy/creating-kubernetes-cluster-on-azure-with-terraform-and-python-using-cdk-for-terraform-8237ffa15092)  

[Managing your GitHub setup with python using the Terraform CDK | Lucas Melin](https://www.lucasmelin.com/managing-your-git-hub-setup-with-python-using-the-terraform-cdk)  

-- init first, then pip install  
cdktf init --template="python-pip" --local  
pip install -r requirements.txt  

From <https://www.lucasmelin.com/managing-your-git-hub-setup-with-python-using-the-terraform-cdk>   

Cdktf init --help  

Infrastructure as Code Using AWS Cloud Development Kit — Patricia Anong (patricia-anong.com)  

Create AWS Infrastructure using CDK for Terraform - Style-Tricks  

Deploy AWS Lambda with CDK for Terraform | by Nathan Bekenov | DAE blog | Medium  

cdktf-ex/lambda-example at main · nbekenov/cdktf-ex (github.com)  

Cdktf Trials with Python | Aaron Addleman  

Creating CloudWatch Alarms using Terraform CDK (Part 2) | Miyuru Tech Blog  

rand 'tech snippets'.hash.next: Terraform CDK Python: spin OCI (Oracle Cloud Infrastructure) VM (spareslant.blogspot.com)  

rand 'tech snippets'.hash.next: Terraform CDK (spareslant.blogspot.com)  

-- multi-stack CDKTF  
rand 'tech snippets'.hash.next: Multi-Stack Terraform CDK (Python) in Oracle Cloud Infrastructure (OCI) (spareslant.blogspot.com)  

wagtail-cloud/main.py at main · tomusher/wagtail-cloud (github.com)  
![image](https://user-images.githubusercontent.com/6020438/177660899-b116f58b-d876-4c05-a502-54570356a327.png)  
