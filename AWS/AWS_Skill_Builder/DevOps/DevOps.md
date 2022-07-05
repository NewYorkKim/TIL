# AWS Cloud Development Kit Primer

> 2022/07/02

- source: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/2000/play/41907/getting-started-with-devops-on-aws;lp=85)



## AWS Cloud Development Kit Introduction

##### What is AWS CDK?

- An open-source software development framework for defining cloud infrastructure as code
- Compiling your source code into an assembly language is a common code-development process
- Think of AWS CDK as a complier that compiles your source code into an AWS CloudFormation template
- Also enables developers to use common code-development practices by offering tools to check for potential problems, identify code differences, and bootstrapping resources needed for deployment

![mod1_what_does_the_aws_cdk_do.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1656748800/uUeSvMrbRxhj_NNRzRgJKw/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/f1WSYwFVJTkWU8H8_hKhS2tEmTTiYy5l8.png)



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

![module2_what_are_constructs.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/gnRIGbouZulnljiw_5okXExLCWWEJUlas.png)



- Can represents a single AWS Cloud resource, such as an Amazon VPC endpoint, or it can represent a single component consisting of multiple AWS resources within a vpc
- AWS CDK uses compositions to define complex constructs
  - A composition establishes a parent-child build hierarchy

![AWS CDK construct code example](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/hPD_EnjC_HZ248ws_tAZK3jJyhiZ963wM.png)



- The composition of constructs means that you can define reusable components and share them like any other code

![module2_reusable_components.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/EBJtL8XbFx3k3vBV_PYnrrNsFDAZzhiVn.png)



- Constructs are implemented in classes that extend the *Construct* base class
- All constructs take three parameters when they are initialized: scope, id, and props
  - Scope: The construct in which this construct is created: `this`
  - Id: The local identifier of the construct that must be unique within this scope: `MyVpc`
  - Props: A set of initialization properties that are specific to each construct and define its initial configuration: `maxAzs`, `cidr`, and `subnetConfiguration`

![TypeScript construct code example with its scope, id, and props initialized for a VPC](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/p7SvSpBgOtWm4zre_EIwObwGXLL6NirSM.png)



- You can build your own constructs when you want to:
  - Organize your project
  - Streamline your deployment processes
  - Package the construct into a npm module
  - Then, publish the construct to npmjs.org to share with developers outside your organization

![module2_building_your_own_constructs.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/2BuUkFpFLx54BecK_f5J5xiTMN4YLcnYd.png)



##### Using Predefined Constructs for AWS resources

- The AWS CDK includes the AWS Construct Library to ensure that developers have access to all AWS resources while building their apps

![AWS CDK construct code highlighting the s3.Bucket class.](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/9oT31vasGDBejEsY_0IAb3-7llPeDDk16.png)



- Levels of constructs
  - The library contains three levels of constructs: AWS CDK, pattern constructs, AWS resource constructs, and AWS CloudFormation resource constructs
  - Level 1 (L1)
    - Directly represents all the AWS resources available in AWS CloudFormation
  - Level 2 (L2)
    - Includes AWS includes AWS resource constructs
  - Level 3 (L3)
    - Are designed to help you complete common tasks in AWS using various resources, such as Fargate container cluster employing an Application Load Balancer

![module2_levels_of_constructs_.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/280T1FsfRaYt--1S_uAkE2vXFKk14lDy2.png)



- AWS CDK pattern constructs
  - Level 3 includes AWS CDK pattern constructs, developed by AWS engineers, and provides opinionated best-practice patterns by default
  - These higher-level constructs stitch together multiple resources and generally represent reference architectures or design patterns to help you complete common tasks in AWS
  - `ecs_patterns.ApplicationLoadBalancedFargateService` construct represents an architecture that includes a Fargate container cluster employing an Application Load Balancer

![module2_AWS_CDK_construct_AWS_engineers.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/Axp27wTtKfcCuAZg_7Y9QRQysb7cM3ioa.png)

![module2_CDK_pattern_constructs.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/WdZ9e2y-Q2rzArmh_0eCCUx6XX1sxHeFz.png)



- AWS resource constructs

  - AWS resource constructs represent AWS resources but with a higher level of purpose

  - Provide the same resource functionality, but they handle many of the details required by AWS CloudFormation resource constructs

![module2_AWS_resource_contructs.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/-2GCn-GFYPZqTSKO_2HAxZ-AKzNH_gZJW.png)



- AWS CloudFormation resource constructs
  - The lowest-level (L1) constructs
  - Mirror the AWS CloudFormation resource types and are updated with each release of AWS CDK

![module2_CFN_resource_constructs.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/uBF-op6salpFc_s0_icaDIgDAlEz8FraB.png)



##### App and Stacks

- The standard AWS CDK development workflow is similar to the common workflow that you use as a developer

![module2_Apps_and_Stacks.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/35iXDRdrjn8Nk9hW_o1GeBcztj7Zu-nXK.png)



- The App construct
  - Every AWS CDK application is represented by the AWS CDK class APP
  - The App construct represents the entire AWS CDK app

![App construct defined as CdkPrimerStack](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/BcWpSo1VwpOHyIwJ_WaIR-4NOQe86N2NC.png)



- Nested stacks
  - AWS CDK gains its deployment power from AWS CloudFormation
  - However, it is also bound by AWS CloudFormation resource limit of 200 resources
  - A way around the resource limit is to create a nested stack

![module2_nested_stacks.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1657033200/LsvhsTmzoLBxveGRv_0y7A/tincan/b450fd4f5b346b88f24b2c75349b1a15f069c464/assets/I60wZKU7T-vLcMN4_x8d81O70Or0zJN2x.png)

