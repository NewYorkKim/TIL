# AWS Cloud Development Kit Primer

> 2022/07/02 ~ ing

- source: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/2000/play/41907/getting-started-with-devops-on-aws;lp=85)



## AWS Cloud Development Kit Introduction

##### What is AWS CDK?

- An open-source software development framework for defining cloud infrastructure as code
- Compiling your source code into an assembly language is a common code-development process
- Think of AWS CDK as a complier that compiles your source code into an AWS CloudFormation template
- Also enables developers to use common code-development practices by offering tools to check for potential problems, identify code differences, and bootstrapping resources needed for deployment

![mod1_what_does_the_aws_cdk_do.png](DevOps/f1WSYwFVJTkWU8H8_hKhS2tEmTTiYy5l8.png)



- Core framework of AWS CDK
  - Constructs
    - The basic building blocks of AWS CDK apps
    - Represents a cloud component and encapsulates everything that AWS CloudFormation needs to create the component
    - AWS Construct Library
  - Stacks
    - A unit of deployment in AWS CDK
  - Apps
    - Your CDK application is an app, and is represented by the AWS CDK App class



##### Importance of AWS CDK for your organization

- Workflow
  - With AWS CDK, you can use your organization's existing code review processes for building cloud infrastructure

- Reuse your infrastructure as a library
  - With AWS CDK, you can design your own reusable components that meet your organization's security, compliance, and governance requirements



##### Advantages of using AWS CDK

- AWS CDK offers benefits, including:
  - Achieving faster deployment by using expressive programming languages for defining infrastructure
  - Incorporating features such as objects, loops, and conditions to improve the ease with which you can define your infrastructure
  - Staying in your integrated development environment (IDE)
  - Writing your runtime code and defining your AWS resources with the same programming language
    - TypeScript, JavaScript, Python, Java, C#
- Additional benefits
  - Use logic (IF statements, for-loops) when defining your infrastructure
  - Use object-oriented techniques to create a model of your system
  - Define high-level abstractions, share them, and publish them to your team, company, or community
  - Organize your project into logical modules
  - Share and reuse your infrastructure as a library
  - Test your infrastructure code using open-standard protocols
  - Use your existing code review workflow
  - Complete code within your IDE



##### How AWS CDK interacts with supported programming languages

- AWS builds the business logic of AWS Construct Library packages in TypeScript, and uses **AWS JSii** to provide mappings to each supported programming
- The code you write in your AWS CDK project is built in the programming language you prefer, and the compiled JavaScript runtime is an implementation of your code
- [AWS JSii GitHub repository](https://github.com/aws/jsii)



## AWS CDK Core Components

##### What are constructs?

- The *core components* that power AWS CDK applications are composed of *apps, stacks, and constructs*
- Constructs are the main building blocks used to form stacks and apps
- Represents a cloud components and encapsulates everything that AWS CloudFormation needs to create the components

![module2_what_are_constructs.png](DevOps/gnRIGbouZulnljiw_5okXExLCWWEJUlas.png)



- Can represents a single AWS Cloud resource, such as an Amazon VPC endpoint, or it can represent a single component consisting of multiple AWS resources within a vpc
- AWS CDK uses compositions to define complex constructs
  - A composition establishes a parent-child build hierarchy

![AWS CDK construct code example](DevOps/hPD_EnjC_HZ248ws_tAZK3jJyhiZ963wM.png)



- The composition of constructs means that you can define reusable components and share them like any other code

![module2_reusable_components.png](DevOps/EBJtL8XbFx3k3vBV_PYnrrNsFDAZzhiVn.png)



- Constructs are implemented in classes that extend the *Construct* base class
- All constructs take three parameters when they are initialized: scope, id, and props
  - Scope: The construct in which this construct is created: `this`
  - Id: The local identifier of the construct that must be unique within this scope: `MyVpc`
  - Props: A set of initialization properties that are specific to each construct and define its initial configuration: `maxAzs`, `cidr`, and `subnetConfiguration`

![TypeScript construct code example with its scope, id, and props initialized for a VPC](DevOps/p7SvSpBgOtWm4zre_EIwObwGXLL6NirSM.png)



- You can build your own constructs when you want to:
  - Organize your project
  - Streamline your deployment processes
  - Package the construct into a npm module
  - Then, publish the construct to npmjs.org to share with developers outside your organization

![module2_building_your_own_constructs.png](DevOps/2BuUkFpFLx54BecK_f5J5xiTMN4YLcnYd.png)



##### Using Predefined Constructs for AWS resources

- The AWS CDK includes the AWS Construct Library to ensure that developers have access to all AWS resources while building their apps

![AWS CDK construct code highlighting the s3.Bucket class.](DevOps/9oT31vasGDBejEsY_0IAb3-7llPeDDk16.png)



- Levels of constructs
  - The library contains three levels of constructs: AWS CDK, pattern constructs, AWS resource constructs, and AWS CloudFormation resource constructs
  - Level 1 (L1)
    - Directly represents all the AWS resources available in AWS CloudFormation
  - Level 2 (L2)
    - Includes AWS includes AWS resource constructs
  - Level 3 (L3)
    - Are designed to help you complete common tasks in AWS using various resources, such as Fargate container cluster employing an Application Load Balancer

![module2_levels_of_constructs_.png](DevOps/280T1FsfRaYt--1S_uAkE2vXFKk14lDy2.png)



- AWS CDK pattern constructs
  - Level 3 includes AWS CDK pattern constructs, developed by AWS engineers, and provides opinionated best-practice patterns by default
  - These higher-level constructs stitch together multiple resources and generally represent reference architectures or design patterns to help you complete common tasks in AWS
  - `ecs_patterns.ApplicationLoadBalancedFargateService` construct represents an architecture that includes a Fargate container cluster employing an Application Load Balancer

![module2_AWS_CDK_construct_AWS_engineers.png](DevOps/Axp27wTtKfcCuAZg_7Y9QRQysb7cM3ioa.png)

![module2_CDK_pattern_constructs.png](DevOps/WdZ9e2y-Q2rzArmh_0eCCUx6XX1sxHeFz.png)



- AWS resource constructs

  - AWS resource constructs represent AWS resources but with a higher level of purpose

  - Provide the same resource functionality, but they handle many of the details required by AWS CloudFormation resource constructs

![module2_AWS_resource_contructs.png](DevOps/-2GCn-GFYPZqTSKO_2HAxZ-AKzNH_gZJW.png)



- AWS CloudFormation resource constructs
  - The lowest-level (L1) constructs
  - Mirror the AWS CloudFormation resource types and are updated with each release of AWS CDK

![module2_CFN_resource_constructs.png](DevOps/uBF-op6salpFc_s0_icaDIgDAlEz8FraB.png)



##### App and Stacks

- The standard AWS CDK development workflow is similar to the common workflow that you use as a developer

![module2_Apps_and_Stacks.png](DevOps/35iXDRdrjn8Nk9hW_o1GeBcztj7Zu-nXK.png)

1. Create the app from a template provided by AWS CDK
2. Add code to the app to create resources within the stack
3. Synthesize one or more stacks in the app to create an AWS CloudFormation template
4. Deploy one or more stacks to your AWS account



- The App construct
  - Every AWS CDK application is represented by the AWS CDK class APP
  - The App construct represents the entire AWS CDK app

![App construct defined as CdkPrimerStack](DevOps/BcWpSo1VwpOHyIwJ_WaIR-4NOQe86N2NC.png)



- Nested stacks
  - AWS CDK gains its deployment power from AWS CloudFormation
  - However, it is also bound by AWS CloudFormation resource limit of 200 resources
  - A way around the resource limit is to create a nested stack

![module2_nested_stacks.png](DevOps/I60wZKU7T-vLcMN4_x8d81O70Or0zJN2x.png)



## AWS CDK Concepts

##### Identifiers

- AWS CDK uses various types of identifiers

- Construct IDs

  - **id**: The most common identifier
  - Must be unique only in the scope in which it is created, which is the first argument when instantiating a construct

  ```typescript
  import * as cdk from '@aws-cdk/core';
  import * as ec2 from "@aws-cdk/aws-ec2";
  import * as ecs from "@aws-cdk/aws-ecs";
  import * as ecs_patterns from "@aws-cdk/aws-ecs-patterns";
  
  export class CdkPrimerStack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
      super(scope, id, props);
  
      const vpc = new ec2.Vpc(this, "MyVpc", {maxAzs: 2});
      const cluster = new ecs.Cluster(this, "MyCluster", {vpc: vpc});
          new ecs_patterns.ApplicationLoadBalancedFargateService(this, "MyFargateService", {
              cluster: cluster,
              taskImageOptions: { image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample") },
              publicLoadBalancer: true
      });
  
  
    }
  }
  const app = new cdk.App();
  new CdkPrimerStack(app, 'CdkPrimerStack');
  new CdkPrimerStack(app, 'CdkPrimerStack2');
  ```

  

- Paths	

  - The constructs in an AWS CDK application form a hierarchy rooted in the App class, and this hierarch is called a path

  ![module3_paths.png](DevOps/Rnk0Ay2QIbp1oPQT_y2tOogIU7EKHC0L4.png)

  

- Unique IDs

  - AWS CDK requires that all identifiers in an AWS CloudFormation template are unique

  ![The unique ID for an AWS::EC2::VPC resource is shown as MyVpcF9F0CA6F.](DevOps/03qLOGiBjltmFiKz_bNhLw0rW439PuytS.png)



- Logical IDs
  - Unique IDs serve as the logical identifiers of resources in the generated AWS CloudFormation templates for thos constructs that represent AWS resources
  - Logical identifiers are sometimes called logical names



##### Environments

- Represents the AWS account and AWS Region in which a stack is deployed
- You can manually override the environment by specifying a different set of values than the default

```typescript
import * as cdk from '@aws-cdk/core';
import * as ec2 from "@aws-cdk/aws-ec2";
import * as ecs from "@aws-cdk/aws-ecs";
import * as ecs_patterns from "@aws-cdk/aws-ecs-patterns";

export class CdkPrimerStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "MyVpc", {maxAzs: 2});
    const cluster = new ecs.Cluster(this, "MyCluster", {vpc: vpc});
    	new ecs_patterns.ApplicationLoadBalancedFargateService(this, "MyFargateService", {
      		cluster: cluster,
      		taskImageOptions: { image: ecs.ContainerImage.fromRegistry("amazon/amazon-ecs-sample") },
      		publicLoadBalancer: true
 	});

  }
}
const app = new cdk.App();
const env1 = { account: '444455556666', region:'us-west-1'};
const env2 = { account: '123456789012', region:'us-west-2'};
new CdkPrimerStack(app, 'CdkPrimerStack', { env: env1 });
new CdkPrimerStack(app, 'CdkPrimerStack2', { env: env2 });
```



- Alternatively, to explicitly specify the target, use two AWS CDK CLI environment variables: *CDK_DEFAULT_ACCOUNT* and *CDK_DEFAULT_REGION*

  - `~/.aws/credentials (Linux & Mac) or %USERPROFILE%\.aws\credentials` (Windows)

  ```
  [default]
  aws_access_key_id=AKIAIOSFODNN7EXAMPLE
  aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  
  [user1]
  aws_access_key_id=AKIAI44QH8DHBEXAMPLE
  aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
  ```

  - `~/.aws/config (Linux & Mac) or %USERPROFILE%\.aws\config` (Windows)

  ```
  [default]
  region=us-west-2
  output=json
  
  [profile user1]
  region=us-east-1
  output=json
  ```

  - `cdk deploy --profile user1` ➡ deploy the app into the *us-east-1* AWS Region



##### Contexts

- Context values are key-value pairs that can be associated with a stack or construct
- AWS CDK uses context to cache information from your AWS account, such as the Availability Zones in your account or the Amazon Machine Image (AMI) IDs used to start your instances
- `cdk context`: To retrieve the cached context values from your AWS account

![Output of cdk context command. Displayed are Two Keys and thier corresponding Values](DevOps/q58MMZEG5cwXSSAm_OUceClaTMck4kCUN.png)

 

- Context Method
  - `HostedZone.fromLookup`: Retrieves the hosted zones in your account
  - `stack.availabilityZones`: Retrieves the supported Availability Zones
  - `StringParameter.valueFromLookup`: Retrieves a value from the Amazon EC2 Systems Manager Parameter Store in the current Region
  - `Vpc.fromLookup`: Retrieves the existing Amazon VPC in your accounts
  - `LookupMachineImage`: Looks up an AMI for use with a Network Address Translation (NAT) instance in an Amazon VPC
  - If a given context isn't available, AWS CDK app notifies the AWS CDK CLI that the context information is missing
  - The CLI then performs the following actions:
    - Queries the current AWS account for the information
    - Stores the resulting context information in the `cdk.context.json` file
    - Runs the AWS CDK app again with the context values



##### Assets

- Are local files, directories, or Docker images that can be bundled into AWS CDK libraries and apps

- An example of a directory that contains the handler code for an AWS Lambda function

- Assets can represent any artifact that the app needs to operate

- With AWS CDK, developers can reference assets from Amazon S3 and Amazon ECR

- Amazon S3 assets

  - Are the local files and directories associated with your app that are package and uploaded to Amazon S3

  ```typescript
  import { Asset } from '@aws-cdk/aws-s3-assets';
  import * as path from 'path';
  
  const imageAsset = new Asset(this, "SampleAsset", {
    path: path.join(__dirname, "images/my-image.png")
  });
  
  new lambda.Function(this, "myLambdaFunction", {
    code: lambda.Code.asset(path.join(__dirname, "handler")),
    runtime: lambda.Runtime.PYTHON_3_6,
    handler: "index.lambda_handler",
    environment: {
      'S3_BUCKET_NAME': imageAsset.s3BucketName,
      'S3_OBJECT_KEY': imageAsset.s3ObjectKey,
      'S3_URL': imageAsset.s3Url
    }
  });
  ```

  

- Docker image assets

  - Images are built from a local Docker context directory using a Dockerfile
  - Images are then uploaded to Amazon ECR by using the AWS CDK CLI or the continuous integration and continuous delivery (CI/CD) pipeline of your app

  ```typescript
  import * as ecs from '@aws-cdk/aws-ecs';
  import * as path from 'path';
  import { DockerImageAsset } from '@aws-cdk/aws-ecr-assets';
  
  const asset = new DockerImageAsset(this, 'MyBuildImage', {
    directory: path.join(__dirname, 'my-image')
  });
  const taskDefinition = new ecs.FargateTaskDefinition(this, "TaskDef", {
    memoryLimitMiB: 1024,
    cpu: 512
  });
  ```

  

## Working with the AWS CDK Toolkit (CLI)

##### AWS CDK Toolkit

- A command line interface tool used to interact with your application
- Use the AWS CDK Toolkit to:
  - Create and run your application
  - Interrogate the application model that you defined
  - Produce and deploy the AWS CloudFormation templates generated by the AWS CDK
- `aws configure`: Initiate the AWS CLI to configure your default profile

- Install AWS CDK Toolkit

  - At the time of this writing, all AWS CDK applications require Node.js 10.3 or later, even if your application is written in Python, Java, or C#

  ```shell
  npm install –g aws-cdk			#install latest version
  npm install –g aws-cdk@X.YY.Z		#install specific version
  ```



- AWS CDK Toolkit command structure

  - All AWS CDK Toolkit commands start with cdk followed by a subcommand
  - Additional options and arguments can follow the subcommand in any order

- Bootstrapping your AWS environment

  - Deploying AWS CDK applications into your AWS account might require that you provision resources the AWS CDK needs to perform the deployment
  - These resources include an S3 bucket for storing large Lambda functions or other necessary assets and AWS Identity and Access Management (IAM) roles that grant permissions necessary to perform deployments
  - The process of provisioning these initial resources is called bootstrapping

  ![Results of running cdk bootstrap in the terminal window](DevOps/ZSIOXfUpACltthm6_vRe6UGmRMRfp0WzN.png)

  

  - `~/.aws/credentials`: For the specified account and Region
  - You can then specify a profile that contains the required credentials

  ```shell
  cdk bootstrap                  # bootstraps default account/region
  cdk bootstrap --profile test   # bootstraps test profile account/region
  ```



- Additionally, using command-line parameters with the cdk bootstrap command offers ways to customize your bootstrapping resources
  - `--bootstrap-bucket-name`: Overrides the name of the Amazon S3 bucket
  - `--bootstrap-kms-key-id`: Overrides the AWS Key Management Service (AWS KMS) key used to encrypt the S3 bucket
  - `--tags`: Adds one or more AWS CloudFormation tags to the bootstrap resources
  - `--termination-protection`: Prevents the bootstrap resources form deletion
