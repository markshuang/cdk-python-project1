-- autoscaling lifecycle hook  
https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples  
-- using user data with lifecycle hook command  
https://www.proud2becloud.com/autoscaling-like-a-pro-how-to-use-ec2-auto-scaling-lifecycle-hooks-the-right-way/  
https://aws.amazon.com/blogs/devops/under-the-hood-aws-codedeploy-and-auto-scaling-integration/  
-- using ssm documents along with lambda function for lifecycle hook  
https://www.bitslovers.com/auto-scaling-lifecycle-hooks/  
https://github.com/clebermasters/AWS-Autoscaling-Lifecycle-Hooks-Save-EC2-Logs/blob/master/lambda_ssm_call.py  
https://lgallardo.com/2018/05/04/asg-lifcecyle-hooks/  
https://github.com/aws-samples/aws-lambda-lifecycle-hooks-function/blob/master/cloudformation/lambda_backup.py  
-- with different scenarios, user data in linux and windows, as well as with lambda functions  
https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples/tree/main/features/lifecycle-hooks  

-- IAM policy, SCP, multi-accounts    
https://aws.amazon.com/blogs/industries/best-practices-for-aws-organizations-service-control-policies-in-a-multi-account-environment/  
https://aws.amazon.com/blogs/security/get-more-out-of-service-control-policies-in-a-multi-account-environment/  

-- terraform lambda  
https://github.com/Pocket/terraform-modules/blob/main/src/base/ApplicationVersionedLambda.ts  
-- lambda target for sqs  
https://github.com/Pocket/fxa-webhook-proxy/blob/09a9ea0e6980a919615d9c46c5f60a84296be8d9/.aws/src/sqsLambda.ts  
https://github.com/Pocket/terraform-modules/blob/40643f03b861151f48e6916adb08819c200ad23d/src/pocket/PocketVersionedLambda.ts  
-- lambda target for evenbridge  
https://github.com/Pocket/terraform-modules/blob/02c1233942f57a860961e260f6b58b21e14da1e5/src/pocket/PocketEventBridgeWithLambdaTarget.ts  
-- lambda target for api gateway in route config    
https://github.com/Pocket/terraform-modules/blob/f8113fead51684fceabad3785fa1f78c00283dec/src/pocket/PocketApiGatewayLambdaIntegration.ts  

-- lambda with [dataarchivefile] in python      
https://github.com/ciaranevans/cdktf-investigation/blob/a807a78edccaa23cf1dff6c8fba1d87e0dc9a4a4/main.py  

-- aws ecs fullstack application, Vue.js as front end, Node.js as backend     
https://github.com/aws-samples/amazon-ecs-fullstack-app-terraform  

-- App2Container  
https://aws.amazon.com/blogs/modernizing-with-aws/generating-ci-cd-pipelines-for-containerized-asp-net-applications-using-aws-app2container/  
https://www.nopcommerce.com/en/demo  
https://aws.amazon.com/blogs/modernizing-with-aws/get-started-with-net-development-on-aws-using-quick-starts/  
https://catalog.us-east-1.prod.workshops.aws/workshops/2c1e5f50-0ebe-4c02-a957-8a71ba1e8c89/en-US/net-modernize-your-app  
https://github.com/aws-samples/aws-modern-application-workshop  
https://catalog.us-east-1.prod.workshops.aws/workshops/02696107-09ac-4313-a6cb-3798048b07d7/en-US  
-- docker file for .NET app  
https://containerise.awsbuilders.cloud/03_containerising/02_dockerfile.html  
-- buildspec for build docker image and push to ECR  
https://containerise.awsbuilders.cloud/05_pipeline/02_buildspec.html  
https://awesome-aws-workshops.com/  
-- microservice extractor for .NET  
https://aws.amazon.com/blogs/modernizing-with-aws/announcing-aws-microservice-extractor-for-net/  
-- porting assistant for .NET, moving .NET to .NET Core on linux    
https://aws.amazon.com/blogs/modernizing-with-aws/migrate-wcf-apps-to-wcfcore-using-porting-assistant/  
-- aws blogs on .NET    
https://aws.amazon.com/blogs/modernizing-with-aws/category/programing-language/dot-net/page/1/  
-- aws samples on .NET (DOTNET)  
https://github.com/orgs/aws-samples/repositories?q=dotnet&type=all&language=&sort=  
-- node js sample app  
https://medium.com/bb-tutorials-and-thoughts/automate-deploying-nodejs-api-docker-image-on-aws-app-runner-through-cloudformation-62f179c3d3cf  
-- .NET container on app runner  
https://billthevestguy.com/2021/11/05/net-and-containers-on-aws-part-2-aws-app-runner/  
-- sample node js with Prometheus  
https://www.tinystacks.com/blog-post/use-multiple-docker-images-on-the-same-ecs-service/  
-- docker file for ubuntu with apach server  
https://bitbucket.org/blog/automating-amazon-elastic-container-ecr-container-builds-using-bitbucket-pipelines  
-- issue with docker's latest tag, avoid it, using build id as tag intead    
https://vsupalov.com/docker-latest-tag/  
https://stevelasker.blog/2018/03/01/docker-tagging-best-practices-for-tagging-and-versioning-docker-images/  
-- Ensure ECR repositories have immutable tags  
https://www.intelligentdiscovery.io/controls/ecr/ecr-immutable-tags  
-- app runner workshop  
https://www.apprunnerworkshop.com/  


-- cdk patterns  
https://aws.amazon.com/blogs/devops/developing-application-patterns-cdk/  

-- app runner  
-- with Java spring framework samples  
https://github.com/aws-samples/aws-solutions-apprunner-vpc-terraform   
https://github.com/aws-samples/aws-apprunner-terraform  
-- app runner networking deep dive  
https://aws.amazon.com/blogs/containers/deep-dive-on-aws-app-runner-vpc-networking/  
https://github.com/awslabs/amazon-app-runner-deploy  
-- app runner with custom domain in terraform  
https://technotrampoline.com/articles/aws-app-runner-for-nodejs-with-docker-and-terraform/  
https://tty.neveragain.de/2021/06/18/app-runner-deep-dive.html  
-- docker file with node.js with express  
https://www.apprunnerworkshop.com/getting-started/dockerfile/  

-- tfsec, with docker file  
https://github.com/aws-samples/aws-cdk-tfsec/blob/main/repos/docker_image/Dockerfile  


-- secrets manager, with resource based policy    
https://github.com/visheshgargavi/visheshgargavi-CDKTF-CDK-for-Terraform/blob/5fee97255b74ceae764ab91ace5b397afe4b52e2/secret_manager/variable/var.ts  
https://github.com/visheshgargavi/visheshgargavi-CDKTF-CDK-for-Terraform/tree/5fee97255b74ceae764ab91ace5b397afe4b52e2/secret_manager  
-- user data for aws linux 2  
https://github.com/aws-samples/route-53-application-recovery-controller-codepipeline-with-terraform/blob/main/modules/application_stack/auto-scaling-group.tf  
-- terraform assume role  
https://learn.hashicorp.com/tutorials/terraform/aws-assumerole  
-- terraform cloud control provider  
https://learn.hashicorp.com/tutorials/terraform/aws-cloud-control?in=terraform/aws  
https://learn.hashicorp.com/collections/terraform/aws  

-- cdktf python unit testing  
https://github.com/hashicorp/terraform-cdk/blob/e70f8ea10062d13ec50a3e4c6b948b8bc041c28b/packages/cdktf-cli/templates/python/main-test.py  

-- cdktf run with tfe  
https://github.com/dgreeninger/terraform-cdk-gke-python/tree/c421a06d62dd99965da923cabfbce8bacb7f30b3  

-- docker provider  
https://github.com/sriazcloud/Terraform-AllClouds-kubernetes/blob/267d2b118547d70bbed90391723e2ec5566b6a18/examples/typescript/docker/main.ts  
-- docker file with nginx:latest  
[https://github.com/skorfmann/drop-kick/blob/dfd98c9e3f77adfe391147eddc8e1cf172c9617b/examples/app/ ](https://github.com/skorfmann/drop-kick/blob/dfd98c9e3f77adfe391147eddc8e1cf172c9617b/examples/app/Dockerfile)  
-- applyTag  with visit pattern  
https://github.com/skorfmann/drop-kick/blob/dfd98c9e3f77adfe391147eddc8e1cf172c9617b/examples/utils.ts  

-- build custom terraform provider  
https://github.com/defn/cloud/blob/14c3875d93053c4b911f722641efd677467d74c9/provider/defn_cdktf_provider_buildkite/__init__.py  

-- azure terraform kubernetes cluster  
https://github.com/kim-hangyeol/hcp/blob/9421cf30712dab014da93707eeee3311dd67102f/Hybrid_Cluster/terraform/create-cluster-azure/main.py  
-- gepp GEPP takes your app and Dockerize it, sets up a Kubernetes cluster K8s   
https://github.com/gurayops/gepp/tree/5fe9661b133d6e2824f696784e4632fb76bf8c31   



07/23/2022  
-- aws samples that contains terraform  
https://github.com/orgs/aws-samples/repositories?q=terraform&type=all&language=&sort=  
-- aws samples with terraform and codebuild  
https://github.com/orgs/aws-samples/repositories?q=terraform+codebuild&type=all&language=&sort=   
https://github.com/aws-samples/devsecops-terraform-dojo-codepipeline   
-- iam role, its policies for codepipeline, terraform  
https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples/blob/main/modules/iam-role/main.tf  
-- codebuild spec for different stages within codepipeline, terraform   
https://github.com/aws-samples/aws-codepipeline-terraform-cicd-samples/tree/main/templates  
https://github.com/aws-samples/route-53-application-recovery-controller-codepipeline-with-terraform  

  
terraform agent's docker file  
https://github.com/Mindera/docker-terraform-aws-agent/blob/master/Dockerfile  
https://github.com/markjgardner/vsts-terraform-agent/blob/master/Dockerfile  
https://docs.dogfood-stage.com/guides/working-with-code/tfc-integration/  
https://learn.hashicorp.com/tutorials/terraform/automate-terraform?in=terraform/automation&utm_source=WEBSITE&utm_medium=WEB_IO&utm_offer=ARTICLE_PAGE&utm_content=DOCS  
https://learn.hashicorp.com/tutorials/terraform/tfe-provider-run-triggers?in=terraform/automation  
https://github.com/hashicorp/learn-terraform-tfe-provider-run-triggers/blob/main/admin.tf  
-- buildspec files for each stage within the codepipeline for terraform, TFLine, TFScan, Checkov      
https://github.com/hands-on-cloud/tf-s3-demo-project  
-- codebuild, codepipeline for deploying terraform resources  
https://hands-on.cloud/how-to-use-codepipeline-cicd-pipeline-to-test-terraform/   
https://github.com/hands-on-cloud/aws-codepipeline-terraform-cicd-pipeline/blob/master/1_pipeline/codebuild.tf  
-- build docker file as custom iamge for codebuild   
https://aws.amazon.com/blogs/devops/extending-aws-codebuild-with-custom-build-environments/  
https://aws.amazon.com/blogs/devops/multi-region-terraform-deployments-with-aws-codepipeline-using-terraform-built-ci-cd/  
-- terraform codepipeline machine learning  
https://aws.amazon.com/blogs/machine-learning/deploy-and-manage-machine-learning-pipelines-with-terraform-using-amazon-sagemaker/  
-- eks blueprint terraform  
https://aws.amazon.com/blogs/containers/bootstrapping-clusters-with-eks-blueprints/  
-- aws ACK blueprint  
https://aws.amazon.com/blogs/opensource/introducing-aws-blueprints-for-crossplane/  
https://aws.amazon.com/blogs/networking-and-content-delivery/running-recovery-oriented-applications-with-amazon-route-53-application-recovery-controller-aws-ci-cd-tools-and-terraform/  
https://aws.amazon.com/blogs/devops/monitor-aws-resources-created-by-terraform-in-amazon-devops-guru-using-tfdevops/  
https://aws.amazon.com/blogs/aws/new-aws-control-tower-account-factory-for-terraform/  
https://aws.amazon.com/blogs/containers/build-and-deploy-a-spring-boot-application-to-aws-app-runner-with-a-ci-cd-pipeline-using-terraform/  
https://aws.amazon.com/blogs/aws/announcing-aws-cloud-control-api/  
https://aws.amazon.com/blogs/containers/how-to-automate-amazon-eks-preventative-controls-in-ci-cd-using-cdk-and-opa-conftest/  
https://aws.amazon.com/blogs/devops/aws-config-rdk-deploying-the-custom-rules-using-the-terraform/  
-- can use it on Lazard's infosec 
https://aws.amazon.com/blogs/devops/continuous-compliance-workflow-for-infrastructure-as-code-part-2/  
https://aws.amazon.com/blogs/opensource/cloud-governance-and-compliance-on-aws-with-policy-as-code/  
https://aws.amazon.com/blogs/networking-and-content-delivery/integrating-network-connectivity-testing-with-infrastructure-deployment/  
https://aws.amazon.com/blogs/developer/build-infrastructure-ci-for-terraform-code-leveraging-aws-developer-tools-and-terratest/  
https://aws.amazon.com/blogs/containers/integrate-amazon-api-gateway-with-amazon-eks/  
https://aws.amazon.com/blogs/developer/running-a-kubernetes-job-in-amazon-eks-on-aws-fargate-using-aws-stepfunctions/  
-- jenkins in fargate, terraform  
https://aws.amazon.com/blogs/devops/building-a-serverless-jenkins-environment-on-aws-fargate/  
https://aws.amazon.com/blogs/developer/provision-aws-infrastructure-using-terraform-by-hashicorp-an-example-of-running-amazon-ecs-tasks-on-aws-fargate/  
https://aws.amazon.com/blogs/compute/introducing-spot-blueprints-a-template-generator-for-frameworks-like-kubernetes-and-apache-spark/  
https://aws.amazon.com/blogs/apn/using-aws-codebuild-and-bridgecrew-to-prevent-misconfigurations-in-aws-cloudformation-and-terraform/  
https://aws.amazon.com/blogs/opensource/accelerate-infrastructure-as-code-development-with-open-source-former2/  
https://aws.amazon.com/blogs/mt/aws-organizations-aws-config-and-terraform/  
https://aws.amazon.com/blogs/apn/modernize-your-ci-cd-pipeline-using-jenkins-x-with-amazon-eks/  


07/21/2022   
-- codepipeline  
https://github.com/abdelilah/cdktf-aws-ecs-app/blob/de6ca38a4a8b4acf61f92ad9e0a8aa1aa622f3e4/resources/ecs-codepipeline.ts  
https://github.com/shazi7804/terraform-cdk-examples/blob/73eba6e24f2d7b1ed4aa674ea034a8545e94f2d0/lib/aws/deployment.ts  
-- deploy azure kubernetes  
https://github.com/shazi7804/cdktf-aws-deployment-anywhere/blob/74180a8b7d1c25b386a4dffbff9377ed1f4fc14a/lib/aws-deployment.ts  
-- pocket codepipeline  
https://github.com/Pocket/data-flows/blob/746c28963cb545ea39a3ff17eda8f4ec7cf3d537/.aws/src/DataFlowsCodePipeline.ts  
-- webhook  
https://github.com/sthuck/duckduckstay/blob/6efb08ad23ef6c715598990253e07c376405bce0/terraform/build-env.ts  
https://github.com/tractr/stack/blob/9d7aafc4e9bce14de3e3d4a5904413914b15b0d8/libs/terraform/component/deployment/src/lib/deployment-pipeline.component.ts  
https://github.com/Pocket/terraform-modules/blob/ec78c378c6ae0c61578d2d298203c6244a447b55/src/pocket/PocketECSCodePipeline.ts  

https://github.com/workflows-sh/do-k8s  
from constructs import Construct  
from cdktf import App, TerraformStack, RemoteBackend, NamedRemoteWorkspace  
from app_stacks.stack_base import BaseStack  

class StackRemoteBackend(BaseStack):  
    def __init__(self, scope: Construct, ns: str,   
                 organization: str,  
                 workspace_name: str):  
        super().__init__(scope, ns)  
        RemoteBackend(self,  
                      organization= organization,  
                      hostname="app.terraform.io",  
                      # name of workspace needs to be passed from subclass  
                      workspaces=NamedRemoteWorkspace(workspace_name),  
        )  

07/16/2022  
-- aws cdk solutions patterns, default behavior, helper for various constructs  
https://github.com/awslabs/aws-solutions-constructs/tree/33e8f17a1d1df5be78882a8a59b54d689fea1e82/source/patterns/%40aws-solutions-constructs/core/lib  
https://github.com/Team-FakeNews/CTFKit/blob/develop/ctfkit/terraform/__init__.py   
https://github.com/philschmid/cdk-samples/blob/6a37732594b8c8d87b6f958605b337cab2ede900/cdktf/README.md  
-- using cloudposse module in cdktf  
 "terraformModules": [  
    "cloudposse/elastic-beanstalk-application/aws@~> 0.11.0"  
  ],  
-- cloudposse modules    
https://github.com/cloudposse/terraform-aws-components/tree/master/modules/  


-- deepmerge in python  
https://github.com/febus982/cdk-platform/blob/e72317c2594cb17dfb369a0bc10e3ee6fe075d47/platform/apps/abstract/base_app.py  

-- api gateway, lambda from pocket  
https://github.com/Pocket/fxa-webhook-proxy/blob/09a9ea0e6980a919615d9c46c5f60a84296be8d9/.aws/src/apiGateway.ts  
-- event bridge   
https://github.com/Pocket/pocket-event-bridge/tree/main/.aws/src  
--  cdk8s  
https://cdk8s.io/docs/latest/plus/container/  

https://github.com/stackmate-io/stackmate/tree/6934617e974cb08c6a384cf568111e11affe5ef6   

--  eks, tls certificate, 8ks,   
https://github.com/OlivierPT/terraform/blob/22991aaee42c5bcd1791e773eac0cc6b82095b68/cdktf-aws-eks/infra/main.ts  
--  good example of creating app using cdktf in typescript  
https://github.com/Pocket/recommendation-api/blob/main/.aws/src/main.ts  
-- can use cdktf_cdktf_provider_aws or "import awsprovider" to search in github  
https://github.com/search?l=Python&p=2&q=%22import+AwsProvider%22&type=Code  
-- using TerraformHclModule  
https://github.com/peytoncasper/tf-cdk-examples/blob/abe661ea4a162b526705ce5f7949bbf9cecc435c/post-provision-steps/main.py  
https://github.com/G4rr/server/blob/b3b75016fbc10ed6928e2af07da57fc86c2ab0dd/api.py  
-- aws organization, sso  
https://github.com/defn/cloud/blob/6b1da436602d969facb879f4041a0eb77e1c7164/src/defn/aws/organizations.py  
-- kms, key policy  
https://github.com/ahmadalibagheri/cdktf-python-aws-kms/blob/f29e6237265c3a1ec60db58275bfa9eaa3185951/main.py  
-- cross-stack  
https://github.com/dhmistry3/cdktf-cross-stack  
-- vpc, subnet, security groups, ec2 with inline user data, db instance, alb, target group, alarm    
https://github.com/Devsharma27/cdktf/blob/afd1ccbcd1c545bdf3a8aef382e52e3d1800951f/matricfilter.py  
-- eks, vpc,  
https://github.com/celeguim/cdktf-aws-python/blob/f43372ba2524e3df79976a883d243d70dd956490/cdktf-aws-python/main.py  
-- docker provider  
https://github.com/sriazcloud/Terraform-AllClouds-kubernetes/blob/267d2b118547d70bbed90391723e2ec5566b6a18/examples/python/docker/main.py  
-- kubenetes provider   "terraformProviders": ["kubernetes@~> 1.11.3"],  
https://github.com/sriazcloud/Terraform-AllClouds-kubernetes/blob/267d2b118547d70bbed90391723e2ec5566b6a18/examples/python/kubernetes/main.py  
-- vpc, cloudfront, s3, acm, codebuild, codepipeline, r53, iam,  waf  
https://github.com/gonzape27/cdktf-boiler-template/tree/cef76883a382edb74e6f3edb5f7ee95100973a48/functions  
-- helm, kubenetes  
https://github.com/pavan8855/enthire/blob/e35565fd8f0f0201c1f5cbe599ba50c4230c7948/main.py  
https://github.com/yobooooi/tdd-terraform-cdk/blob/d251a8d354e7232f66318915e0e600fad32cd41b/main.py  
-- dynamodb replication  
https://github.com/Kshitiz-Arya/DynamoDB-replication/tree/c5920bbb06cf4132427aa2163553cad1e71e8f7e  
-- aws lightsail  
https://github.com/MongoExpUser/UNEMY-Stack-on-AWS-Lightsail/tree/fbf449aa9c854337ad782733fd823f7a6e0ffd62  

-- typescript cdktf  
-- vpc, cloudfront, r53, s3, acm, 
https://github.com/zaqqaz/terraform-typescript-frontend-infrastructure/tree/71cbc15b23f8d482bb09f8e39ee22ae990f66a09/terraform/src  
-- tlsprovider, certificate, alb, target, ecs    
https://github.com/vaspoz/pgadmin-aws/blob/0946294e6d2d3b204c7fb739f274141618c592cf/infra_resources/pgadmin_alb.ts  
-- tlsprovider, privatekey  
https://github.com/mkm29/cdktf-ec2/blob/a6258742733b2b7636a4413bf69c367617e03ee1/main.ts  
-- python script, saving private key to file using local provider    
https://github.com/spareslant/oci_multi_stack_terraform_cdk_python_v2/blob/76e05495ef46c7b23c84c1d772f886d6eeb38166/systemsAndApps.py  

07/15/2022   
-- ssh using terraform  
https://docs.microsoft.com/en-us/azure/developer/terraform/create-linux-virtual-machine-with-infrastructure  
https://www.phillipsj.net/posts/generating-ssh-keys-with-terraform/  
https://stackoverflow.com/questions/67389324/create-a-key-pair-and-download-the-pem-file-with-terraform-aws  
https://github.com/cloudposse/terraform-tls-ssh-key-pair/blob/master/main.tf  
https://stackoverflow.com/questions/59473690/how-to-extract-sensitive-output-variables-in-terraform  
https://faun.pub/how-to-create-ssh-keys-with-terraform-a615dfc631c1  
https://www.linuxfixes.com/2022/06/solved-how-do-i-create-ssh-key-in.html   
https://scripting4ever.wordpress.com/2020/11/15/automate-ssh-key-generation-and-ec2-deployment-using-terraform-in-windows-environment/  
https://github.com/kujalk/Terraform-EC2-SSH/blob/main/main.tf  
-- create ec2 with nginx in terraform  
https://awstip.com/how-to-create-an-nginx-instance-in-aws-using-terraform-feb6af12749a  
https://www.clickittech.com/devops/terraform-best-practices/  
https://opensourcelibs.com/libs/terraform-modules  
https://opensourcelibs.com/lib/tf_aws_bastion_s3_keys  

07/14/2022  
-- s3 web site, cloudfront and distribution  
https://github.com/Maed223/cdktf-integration-serverless-python-example/blob/main/frontend/index.py  
-- api, lambda backend, lambda pacakge  
https://github.com/Maed223/cdktf-integration-serverless-python-example/blob/main/posts/api/index.py  

-- cdk solutions patterns  
https://docs.aws.amazon.com/solutions/latest/constructs/welcome.html  
https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs  

07/13/2022  
-- aws workshop  
https://awesome-aws-workshops.com/#enterprise-customers  
https://workshops.aws/  

-- api gateway  
https://github.com/Pocket/terraform-modules/blob/main/src/pocket/PocketApiGatewayLambdaIntegration.ts  

-- windows powershell in userdata  
https://aws.amazon.com/blogs/infrastructure-and-automation/logging-windows-amazon-ec2-userdata-activity-in-amazon-cloudwatch/  
https://aws.amazon.com/blogs/developer/deploy-an-amazon-ecs-cluster-running-windows-server-with-aws-tools-for-powershell-part-1/  
https://aws.amazon.com/blogs/developer/installing-scheduled-tasks-on-ec2-windows-instances/  
https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-windows-user-data.html  
-- terraform userdata  
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#user_data  
https://stackoverflow.com/questions/67120939/executing-powershell-script-on-remote-windows-ec2-instance-in-terraform  

-- example of using powershell on userdata for windows instance  
https://skundunotes.com/2021/11/07/working-with-aws-ec2-user-data-and-terraform/  
https://github.com/kunduso/ec2-userdata-terraform/tree/add-userdata/user_data  

https://github.com/andreswebs/terraform-aws-ec2-userdata-ad-join/tree/main/tpl  
https://gmusumeci.medium.com/how-to-deploy-a-windows-server-ec2-instance-in-aws-using-terraform-dd86a5dbf731  

powershell  "userdata" terraform  on google  

-- terraform eks helm  
https://aws.amazon.com/blogs/startups/from-zero-to-eks-with-terraform-and-helm/  
https://github.com/hashicorp/terraform-provider-aws/tree/main/examples/eks-getting-started  
-- ec2, autoscaling, lifecycle   
https://github.com/aws-samples/amazon-autoscaling-mac1metal-ec2-with-terraform/blob/main/terraform-aws-ec2-mac/main.tf  
-- security group, autoscaling, elb, target group, iam role, congnito, custom resource  
https://github.com/aws-samples/cdktf-aws-elb-cognito-auth/blob/main/src/app.ts  
-- api gateway, cognito, dynamoDB, lambda    
https://github.com/hadock/CDKTF-From-Zero-To-Hero/blob/main/Assets/Demo/applications/backends/myapp1/index.ts  
-- ecs vs eks  
https://www.cloudzero.com/blog/ecs-vs-eks  
So, if you are building containerized systems where the containerized part is just one piece of a broader AWS ecosystem, ECS is the logical choice. If you’ve built a system using a lot of AWS platform services, such as RDS, SNS, S3, SQS, Eventridge, DynamoDB, and need some additional capabilities, you may want to use ECS.

However, if you’re trying to isolate all your applications, logic, and systems so that you have maximum portability, then EKS is the tool to consider.

Companies often choose EKS over ECS because they fear cloud lock-in. And they believe that if they build their applications using only the building blocks provided by Kubernetes, that they will have maximum portability. In other words, if there’s an issue with their cloud provider, they can pick up all their containers and move to a different cloud provider.

However, the most cost-effective, efficient, and well-architected systems are the ones that instead treat the cloud provider as the operating system and they make a clear commitment to the platform.

Making this definitive choice will save the team a lot of engineering time that would have been otherwise spent on pursuing a multi-cloud strategy. The time saved would allow them to build functionality faster and deliver more features to market. See this blog for a more detailed look comparing multi-service and multi-cloud strategies.

So, if you’ve embraced a multi-service strategy with AWS as your anchor cloud provider, ECS is almost certainly a better choice. The only challenge with ECS is that it’s harder to find and hire talent because ECS is not as universal as Kubernetes or EKS.  

https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes/  
ECS is really simple to deploy. After all, it was designed to be a simple API for creating containerized workloads without any complex abstractions. You get no control plane, so once your cluster is set up, you can configure and deploy tasks directly from the AWS management console. 

Deploying clusters on EKS is a bit more complex and requires expert configuration. You need to configure and deploy pods via Kubernetes first because EKS is just another layer for creating K8s clusters on AWS. 

So compared to ECS, you need more expertise and operational knowledge to deploy and manage applications on EKS.  

https://sysdig.com/learn-cloud-native/kubernetes-security/aws-eks-with-and-without-fargate-understanding-the-differences/  
Let’s start by defining the two main services that Amazon offers for deploying containerized applications:

Elastic Kubernetes Service (EKS): EKS is a container deployment service based on open source Kubernetes. You could also call it a Kubernetes distribution or Kubernetes-as-a-Service.
Elastic Container Engine (ECS): ECS is a container deployment service powered by a proprietary container orchestration engine that Amazon developed itself. AWS built ECS back in the days of the “orchestrator wars,” before it was clear that Kubernetes would become, by far and away, the leading container orchestration platform.
Both of these services let you do basically the same thing, albeit in slightly different ways: deploy containerized applications using an orchestration layer that is hosted in the AWS cloud. In most cases, ECS and EKS also rely on infrastructure that is hosted by AWS.

(The exception is if you use EKS Anywhere or if you run ECS or EKS via AWS Outposts, AWS’s hybrid cloud framework. In these situations, you can use private infrastructure to host your applications, even though the orchestration control plane would remain hosted in the AWS public cloud.)  

-- fargte or not  
Fargate gives you less control in various ways. Not only do you not control cluster sizing, but you also can’t specify configuration variables like HostPort and HostNetwork for containers running in Fargate mode. You also can’t run containers in privileged mode, and you can’t configure DaemonSets.

In general, then, Fargate makes most sense when you don’t need fine-tuned control over how your containers run. If you need as much control as possible, use EKS in standard mode.  


https://medium.com/@Nautilus_Technologies/ecs-vs-eks-vs-fargate-what-to-choose-in-2022-6fd8c65fbcd8  

EKS

If you are using Kubernetes already and your team wants to deploy their Kubernetes cluster on AWS infrastructure.
EKS is the right choice if you want to migrate your workloads from AWS to a different cloud provider in the future.
If you want a secure, highly available container service with observability across all Kubernetes deployment, EKS is a better option.   


07/12/2022  
-- api gateway integration  
https://aws.amazon.com/blogs/architecture/use-direct-service-integrations-to-optimize-your-architecture/  
https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-application-load-balancers/  
https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/direct-integrations.html  
https://aws.amazon.com/blogs/architecture/category/application-services/amazon-api-gateway-application-services/  
https://aws.amazon.com/blogs/architecture/using-api-gateway-as-a-single-entry-point-for-web-applications-and-api-microservices/  
https://aws.amazon.com/blogs/architecture/things-to-consider-when-you-build-rest-apis-with-amazon-api-gateway/  
https://aws.amazon.com/blogs/compute/category/mobile-services/amazon-api-gateway/  
https://aws.amazon.com/blogs/compute/performing-canary-deployments-for-service-integrations-with-amazon-api-gateway/  
https://aws.amazon.com/blogs/compute/troubleshooting-amazon-api-gateway-with-enhanced-observability-variables/  

07/11/2022  
permissions boundary  
https://aws.amazon.com/blogs/security/use-tags-to-manage-and-secure-access-to-additional-types-of-iam-resources/  
https://aws.amazon.com/blogs/apn/how-cleardata-enforces-data-locality-with-aws-iam-permission-boundaries/  
https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/  
https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/  
https://aws.amazon.com/blogs/apn/easily-delegate-responsibilities-using-aws-permissions-boundaries-and-kion/  
https://aws.amazon.com/blogs/security/how-to-implement-the-principle-of-least-privilege-with-cloudformation-stacksets/  
https://aws.amazon.com/blogs/architecture/field-notes-how-factset-balances-developer-velocity-with-governance-using-aws-iam/  
https://aws.amazon.com/blogs/devops/cdk-corner-march-2021/  
https://aws.amazon.com/blogs/compute/operating-serverless-at-scale-keeping-control-of-resources-part-3/  
https://aws.amazon.com/blogs/security/how-to-control-access-to-aws-resources-based-on-aws-account-ou-or-organization/  



07/10/2022   
-- apprunner in multi-region  
https://github.com/aws-samples/apprunner-multiregion   
-- aws integration and automation repo  
https://github.com/aws-ia  
https://github.com/orgs/aws-ia/repositories?type=all  
https://aws.amazon.com/blogs/mt/introducing-amazon-eks-observability-accelerator/  
-- aws blogs on terraform  
https://aws.amazon.com/search/?searchQuery=terraform#facet_type=blogs&limit=25&page=1&sortResults=modification_date%20desc  
https://aws.amazon.com/blogs/security/top-2021-aws-service-launches-security-professionals-should-review-part-2/  
https://aws.amazon.com/blogs/developer/provision-aws-infrastructure-using-terraform-by-hashicorp-an-example-of-web-application-logging-customer-data/  
https://github.com/aws-samples/aws-ingesting-click-logs-using-terraform  
https://aws.amazon.com/blogs/devops/multi-region-terraform-deployments-with-aws-codepipeline-using-terraform-built-ci-cd/  
https://aws.amazon.com/blogs/devops/monitor-aws-resources-created-by-terraform-in-amazon-devops-guru-using-tfdevops/  
https://github.com/stacklet/tfdevops  
https://aws.amazon.com/blogs/devops/aws-config-rdk-deploying-the-custom-rules-using-the-terraform/  
https://aws.amazon.com/blogs/devops/secure-and-analyse-your-terraform-code-using-aws-codecommit-aws-codepipeline-aws-codebuild-and-tfsec/  
https://aws.amazon.com/blogs/devops/continuous-compliance-workflow-for-infrastructure-as-code-part-2/  
--using terraform to create serverless jenkins on aws fargate  
https://aws.amazon.com/blogs/devops/building-a-serverless-jenkins-environment-on-aws-fargate/  
-- corporate DevOps lesson Cloud Platform team, very similar to Lazard  
https://aws.amazon.com/blogs/devops/transforming-devops-for-a-fintech-on-aws/  
https://aws.amazon.com/blogs/compute/implementing-attribute-based-instance-type-selection-using-terraform/  
-- terraform autoscaling for ec2  
https://aws.amazon.com/blogs/compute/implementing-autoscaling-for-ec2-mac-instances/  
-- terraform Ec2 refresh  
https://aws.amazon.com/blogs/compute/introducing-instance-refresh-for-ec2-auto-scaling/  
-- aws config terraform  
https://aws.amazon.com/blogs/mt/how-to-deploy-aws-config-conformance-packs-using-terraform/  
-- vpc endpoint, cloudwatch in terraform  
https://aws.amazon.com/blogs/mt/monitor-network-throughput-of-interface-vpc-endpoints-using-amazon-cloudwatch/  
-- aws organization, aws config, terraform  
https://aws.amazon.com/blogs/mt/aws-organizations-aws-config-and-terraform/  
-- ssm patching, terraform  
https://aws.amazon.com/blogs/mt/software-patching-with-aws-systems-manager/  
-- cmdb asset, sqs, lambda, dynamoDB, jenkins for deployment, terraform  
https://aws.amazon.com/blogs/mt/building-a-fully-automated-dow-jones-asset-tracking-system-on-aws/  
-- step function for orchestrating blue/green eks deployment, 
https://aws.amazon.com/blogs/startups/using-aws-to-build-tools-that-will-design-tomorrows-green-infrastructure/  
-- Integrating Existing Applications Into DevOps with AWS Amplify | Front-End Web & Mobile  
https://aws.amazon.com/blogs/mobile/4707-2/  
https://aws.amazon.com/blogs/startups/from-zero-to-eks-with-terraform-and-helm/  
-- eks blueprint terraform  
https://aws.amazon.com/blogs/containers/bootstrapping-clusters-with-eks-blueprints/  
-- windows workload eks terraform  
https://aws.amazon.com/blogs/containers/running-windows-workloads-on-a-private-eks-cluster/  
-- multi-cluster eks terrform  
https://aws.amazon.com/blogs/containers/onfidos-journey-to-a-multi-cluster-amazon-eks-architecture/  
https://aws.amazon.com/blogs/containers/how-to-automate-amazon-eks-preventative-controls-in-ci-cd-using-cdk-and-opa-conftest/  
https://aws.amazon.com/blogs/containers/setting-up-a-bottlerocket-managed-node-group-on-amazon-eks-with-terraform/  


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
