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



### AWS Global Infrastructure

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




### AWS Well-Architected Framework

- Operational Excellence
  - The ability to run and monitor systems to deliver business value and continually improve supporting processes and procedures
  - Performing operations as code, annotating documentation, anticipating failure, and frequently making small, reversible changes
- Security
  - The ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies
  - Automate security best practices when possible
  - Apply security at all layers
  - Protect data in transit and at rest
- Reliability
  - The ability of a system to:
    - Recover from infrastructure or service disruptions
    - Dynamically acquire computing resources to meet demand
    - Mitigate disruptions such as transient network issues or misconfigurations
  - Testing recovery procedures, scaling horizontally to increase aggregate system availability, and automatically recovering from failure
- Performance Efficiency
  - The ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve
  - Experimenting more often, using serverless architectures, and designing systems to be able to go global in minutes
- Cost Optimization
  - The ability to run systems to deliver business value at the lowest price point
  - Adopting a consumption model, analyzing and attributing expenditure, and using managed services to reduce the cost of ownership

![image-20220531232222094]([Cloud_Computing]Introduction_to_Cloud_101.assets/image-20220531232222094.png)



### Costs & Billing

##### Total Cost of Ownership

The __Total Cost of Ownership (TCO)__ is a financial metric that is used to estimate and compare direct and indirect costs of a product or a service. It typically includes the actual costs of:

- Procurement
- Management
- Maintenance
- Decommissioning of hardware resources

![image-20220531232640109]([Cloud_Computing]Introduction_to_Cloud_101.assets/image-20220531232640109.png)

![image-20220531232719935]([Cloud_Computing]Introduction_to_Cloud_101.assets/image-20220531232719935.png)



##### AWS pricing models

- Pay-as-you-go
- Save when you reserve
- Pay less by using more



##### AWS Free Tier

- Always free 
- 12 months free
- Trials