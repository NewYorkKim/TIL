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



##### AWS CDK Demonstration



