---- Can look at the terraform modules (typescript) at pocket site, use them as models to create corresponding ones in python 
terraform-modules/src/base at main · Pocket/terraform-modules (github.com)  

-- search for cdktf python projects in Github
Search · cdktf (github.com) 
--search for "Terraform cdk" in github
Search · "Terraform CDK" (github.com) 

-- aws config
cdktf-ex/main.py at main · nbekenov/cdktf-ex (github.com)  

cmclaughlin/hashiconf-cdktf-2021 (github.com)  

Pocket/data-flows: Pocket data flows orchestrated using Prefect (github.com)  

cdktf/main.py at main · swethamothe/cdktf (github.com)  

cdktf/main.py at main · Devsharma27/cdktf (github.com)  

cdktf-get-started/main.py at main · ibm-xaas/cdktf-get-started (github.com)

-- ecs, rds
cdktf-python/main.py at main · byhbt/cdktf-python (github.com)

-- eks, helm with both aws provider and vpc, eks module 
pavan8855/enthire: EKS using terraform-cdk (github.com)

-- vpc, lambda, api gateway
TerraformCdkNotesDemo/main.py at master · eladrapoportcybr/TerraformCdkNotesDemo (github.com)

-- python invoke with ckdtf
vsuzdaltsev/terraform-cdk-examples: terraform-cdk (https://github.com/hashicorp/terraform-cdk) extended examples

--cdktf workshop, not much, can be ignored
chefgs/tfcdk: Terraform CDK Sample Workouts (github.com)

-- ecs
ContainersFromTheCouch-terraform-cdk-example/main.py at master · adamjkeller/ContainersFromTheCouch-terraform-cdk-example (github.com)

-- vpc, s3, rds, cache, ecr,
tomusher/wagtail-cloud: Terraform CDK constructs for deploying Wagtail to various cloud providers (github.com)

-- multi-stack v2
spareslant/oci_multi_stack_terraform_cdk_python_v2 (github.com)  

-- alb, ecs, rds, ssm, log
byhbt/cdktf-python: Project for exploring TFCDK (github.com)  

--vpc, subnet, internet gateway, route table, eks
cdktf-aws-python/main.py at main · celeguim/cdktf-aws-python (github.com)

-- using account, profile for different account and its profile for deployment
cdktf-ex/main.py at main · nbekenov/cdktf-ex (github.com)

-- static website on s3
cdktf-python-aws-staticwebsite/main.py at main · bjiusc/cdktf-python-aws-staticwebsite (github.com)

-- config and custom construct
cdktf-demo/main.py at main · caning01/cdktf-demo (github.com)

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
cdktf-cross-stack/main.py at master · dhmistry3/cdktf-cross-stack (github.com)

-- google
walkerk1980/cdktf_gcp_vm_unifi: terraform cdk stack to deploy Unifi controller on GCP (github.com)

-- R53,
cdktf-boiler-template/main.py at main · gonzape27/cdktf-boiler-template (github.com)

-- codepipeline
cdktf-boiler-template/codepipeline.py at main · gonzape27/cdktf-boiler-template (github.com)
-- codebuild, codepipeline,R53, cloudfront, certificate, iam
cdktf-boiler-template/functions at main · gonzape27/cdktf-boiler-template (github.com)

-- vpc, subent, ec2, instance profile
cdktf-samples-python/main.py at main · shazi7804/cdktf-samples-python (github.com)

-- github repo
github-terraform-cdktf/main.py at develop · vishnu-chegondi/github-terraform-cdktf

-- google
gcp-cdktf-example/main.py at main · lmayorga1980/gcp-cdktf-example (github.com)

-- serverless, S3, cloudfront, iam, lambda, dynamoDB, API gateway
Maed223/cdktf-integration-serverless-python-example: This repo contains an end to end example in Python for a serverless web application hosted on AWS and deployed with the CDK for Terraform. Please refer to the guide for more information. (github.com)

-- ssm
tdd-terraform-cdk/main.py at master · yobooooi/tdd-terraform-cdk (github.com)

--vpc, subnet, token
https://github.com/chandler-mcfly/terraformAWSCdktfPython/blob/main/main_edited.py

-- api gateway, lambda, aws config, waf, aws firewall manager
nbekenov/cdktf-ex: Example of using Terraform CDK (github.com)

-- Developer's Helper to Docker, Kubernetes, and Terraform. Fully automatic, without any config or question
gepp/main.py at main · gurayops/gepp (github.com)

Creating Kubernetes Cluster on Azure with Terraform and Python using CDK for Terraform | by Guray Yildirim | Medium

Managing your GitHub setup with python using the Terraform CDK | Lucas Melin

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
