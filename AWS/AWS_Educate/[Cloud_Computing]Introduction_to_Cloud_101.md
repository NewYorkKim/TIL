# Introduction to Cloud 101

> 2022/05/28 ~ ing

- source: [AWS Educate](https://aws.amazon.com/education/awseducate/)



## Introduction to Cloud 101

##### Why learn about the cloud?

- Demand for cloud computing skills is increasing
- Cloud computing skills are relevant for all IT professionals
- Cloud certification validates knowledge and skills



## Introduction to Cloud Computing

##### Why cloud computing?

- IT assets as programmatic resources to quickly set up and tear down resources
- Access resources dynamically for __agility__ and __flexibility__ to meet customer needs
- Pay-as-you-go to test and use the system without being fully committed



##### Definition of cloud computing

Cloud computing is the on-demand delivery of IT resources over the internet with pay-as-you-go pricing.

- __On-demand delivery__: A cloud provider has the resources you need, when you need them

- __IT resources over the internet__: Servers, networks, storage, development tools, and applications

- __Pay-as-you-go__: Pay only for what you need when you use it



##### Six benefits of cloud computing

1. Trade upfront expense for variable expense
2. Stop spending money to run and maintain data centers
3. Stop guessing capacity
4. Benefit from massive economies of scale
5. Increase speed and agility
6. Go global in minutes



##### Deploying to the cloud

Cloud service and deployment methods provide different levels of control, flexibility, and management.

Deployment models include

- __Infrastructure as a service (IaaS)__
  - Contains the basic building blocks for cloud IT
  - Provides access to networking features, computers (virtual or on dedicated hardware), and data storage space
  - Provides the highest level of flexibility and management control over your IT resources
  - EC2, S3, RDS, and Route 53

- __Platform as a service (PaaS)__
  - Removes the need for organizations to manage the underlying infrastructure (usually hardware and operating systems)
  - They can focus on the deployment and management of applications
  - These tools give developers the ability to be more efficient because they don't need to worry about resource procurement, capacity planning, software maintenance, and patching
  - Elastic Beanstalk

- __Software as a service (SaaS)__
  - A completed software product that the service provider runs and manages
  - With a SaaS offering, you do not have to think about how the service is maintained or how the underlying infrastructure is managed
  - You only must think about how you will use that particular piece of software
  - video meeting sites, email sites, file sharing sites, and messaging apps


Deployment strategies include

- __Cloud__
  - In a cloud-based deployment model, you can migrate existing applications to the cloud, or you can design and build new applications in the cloud
  - You can build those applications on low-level infrastructure that requires your IT staff to manage them
  - You can build them by using higher-level services that reduce the management, architecting, and scaling requirements of the core infrastructure

- __Hybrid__
  - In a hybrid deployment, cloud-based resources are connected to on-premises infrastructure
  - You can integrate cloud-based resources with legacy IT applications

- __On-premises__
  - Also known as a private cloud deployment
  - In this model, resources are deployed on premises by using virtualization and resource management tools
  - Increase resource utilization by using application management and virtualization technologies


Each type of deployment model and strategy has a shared responsibility between you and the cloud service provider.



## Introduction to AWS

##### AWS benefits

- On-demand access to over 175 services cloud-based services
- Pay-as-you-go pricing
- No upfront capital expenses or commitments
  - The ability to try a lot of experiments
  - Not having to live with the collateral damage of failed experiments
- Toolbox of high-end services



##### AWS Global Infrastructure

- Region
  - A physical location around the world where data centers are clustered together
- Availability Zone
  - A zoned area within a Region that can harbor one or more data centers (typically three)
  - House all the hardware devices that AWS offers
- Edge Location
  - Are connected to the AWS Regions through the AWS network across the globe
  - They link with tens of thousands of networks for improved origin fetches and dynamic content acceleration



##### AWS Global Infrastructure benefits

- Performance
- Availability
- Security
- Reliability
- Scalability
- Low Cost



##### Shared responsibility

![image-20220529201134485]([Cloud_Computing]Introduction_to_Cloud_101.assets/image-20220529201134485.png)

- Customers are responsible for the security of everything that they create and put __IN__ the AWS Cloud

  - User access
  - Encryption

- AWS manages the security __OF__ the cloud, specially the physical infrastructure that hosts your resources, which include:

  - Physical security of data centers
  - Hardware and software infrastructure
  - Network infrastructure
  - Virtualization infrastructure

  