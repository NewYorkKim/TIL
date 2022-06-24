# Getting Started with DevOps on AWS

> 2022/06/21 ~ ing

- source: [AWS Skill Builder](https://explore.skillbuilder.aws/learn/course/2000/play/41907/getting-started-with-devops-on-aws;lp=85)



## Introduction to DevOps

##### What Is DevOps?

- DevOps emphasizes **better collaboration and efficiencies** so teams can innovate faster and deliver higher value to business and customers



![An infinity loop formed by the software lifecycle stages is a common depiction of the ongoing collaboration and efficiencies suggested by DevOps.](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1655827200/B4TTCa1aVTfAZDnVr5mS9Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/fWsC1cyKiH4aaLvB_CYv4rrnC2UUazpsm.png)



- DevOps is short for Development (Dev) and Operations (Ops)
- **Dev**: people and processes that create software

- **Ops**: The teams and processes that deliver and monitor the software

- DevOps is a combination of:
  - Cultural philosophies for removing barriers and sharing end-to-end responsibility
  - Processes developed for speed and quality, that streamline the way people work
  - Tools that align with processes and automate repeatable tasks, making the release process more efficient and the application more reliable



##### Problems with Traditional Development Practices

- Waterfall development projects

  - Are slow, not iterative, resistant to change, and have long release cycles

  - Requirements are rigid, set at project start, and will likely not change

  - Development phases are siloed, each starting after the previous phase has ended

  - Testing and security come after implementation, making corrective actions responsive and expensive

 

![Development phases supported by siloed and specialized teams cause delays and are costly.](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1655827200/B4TTCa1aVTfAZDnVr5mS9Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/j_Nv_xAfixC0CuJA_Y2nQWshkYs7a7SSU.png)



- Monolithic applications

  - Are hard to update and deploy

  - Are developed and deployed as a unit, so when changes are made, the entire application must be redeployed

  - Have tightly coupled functionality, so if the application is large enough, maintenance becomes an issue because developers have a hard time understanding the entire application

  - Are implemented using a single development stack, so changing technology is difficult and costly



##### Why DevOps?

- [Accelerate State of DevOps 2019 Report](https://services.google.com/fh/files/misc/state-of-devops-2019.pdf)

![Source: Accelerate State of DevOps 2019, DevOps Research and Assessment (DORA)](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1655827200/B4TTCa1aVTfAZDnVr5mS9Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/Yk-qXajQSpITY_9H_jNMjFOR-QD6vD_Rv.png)



- The benefits of DevOps

![m1_whydevops2.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1655827200/B4TTCa1aVTfAZDnVr5mS9Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/Ksws8--SZ09uws65_VqktCOya5QHnGAky.png)



## DevOps Methodology

##### DevOps Culture

1. Create a highly collaborative environment
2. Automate when possible
3. Focus on customer needs
   - **Customer first**
4. Develop small and release often
5. Include security at every phase
6. Continuously experiment and learn
7. Continuously improve



##### DevOps Practices

1. Communication and collaboration
2. Monitoring and observability
   - Logs report on discrete events, such as warnings
   - Metrics capture health and performance information, such as request rate and response time
   - Traces report on transactions and the flow of data across a distributed system, such as one comprised of microservices
3. Continuous integration (CI)
4. Continuous delivery / continuous deployment (CD)
5. Microservices architecture
6. Infrastructure as code



- DevOps lifecycle stages

![m2devoplifecyclestagesepng.png](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1655827200/B4TTCa1aVTfAZDnVr5mS9Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/OuvWgnqgR3sPM_k2_YbZDu2_Tf8JnkJqp.png)



- CI/CD pipeline
  - Assures code quality, security, and fast, consistent deployments by repeatably progressing through the pipeline
  - Requires a well-integrated tool chain



##### DevOps Tools

- Cloud
  - AWS
- Development
  - IDEs: AWS Cloud9, IntelliJ, Eclipse, Visual Studio Code
  - SDKs: AWS SDK for Java, iPhone SDK
  - Source code repositories: GitHub, AWS CodeCommit
- CI/CD
  - Build tools: Jenkins, Travis CI, AWS CodeBuild
  - Source control tools, repositories: Git, AWS CodeCommit
  - Deployment tools: AWS CodeDeploy, AWS CloudFormation
  - Pipeline automation tools: AWS CodePipeline, Jenkins, GitLab
- Infrastructure automation
  - Infrastructure automation tools: AWS CloudFormation, Terraform, AWS Elastic Beanstalk
  - Configuration management tools: Chef, Puppet, AWS OpsWorks
- Containers and serverless
  - Serverless services: AWS Lambda, AWS Fargate
  - Container services:
    - Runtimes: Docker, Continerd
    - Orchestration: Amazon Elastic Container Service (Amazon ECS), Kubernetes, Amazon Elastic Kubernetes Service (Amazon EKS)
- Monitoring and observability
  - AWS X-Ray, Amazon CloudWatch, AWS Config, AWS CloudTrail



## Amazon's DevOps Transformation

- In the early 2000s, the amazon.com retail website was a large architectural monolith
- Amazon quickly realized that they were slowed down by the development architecture and the organizational structure
- Something needed to change for Amazon to increase the speed of development and velocity of deployment to focus on customer needs

![ Siloed Development, Testing, and Operational teams](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1656072000/i9XlJtgBw-huDjMwIBxq_Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/m00bf1BauwYKsygK_AhXvJlLCp7wVjjID.png)



- Amazon decoupled development, moving towards a **service-oriented architecture**

- They also created small, cross functional two-pizza teams consisting of 8-10 people

  - Two-pizza teams aligned with services

    ![Two-pizza teams aligned with services](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1656072000/i9XlJtgBw-huDjMwIBxq_Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/xZxru9OgOByqiHRv_VB11OutPVbIfTI9d.png)

- They realized that manual processes, hand-offs, and common release cycles were still causing delays. 

- The monolithic architecture was completely decoupled into single-purposed services and soon became a **microservices solution**

  - Two-pizza teams focusing on microservices solutions

    ![Two-pizza teams focusing on microservices solutions](https://assets.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1656072000/i9XlJtgBw-huDjMwIBxq_Q/tincan/674187_1645473379_p1fsetlfoloo1rhbas410e1pe9o_zip/assets/XKAjwmXmY0s2Ju4n_1FuJvRWxj9jK-r0N.png)



- Amazon wanted agility, and transformation became their foundation for adopting DevOps



##### Decompose for agility
