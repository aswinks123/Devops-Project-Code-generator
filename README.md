<b>ABSTRACT</b>

Continuous Integration/Continuous Deployment (CI/CD) is a development approach that helps streamline the software development process by automating various stages of the software development lifecycle. More than that, the primary aim of this project is to create a Continuous Integration/Continuous Deployment pipeline for a QR code generator and scanner application. The application will be developed using Python and deployed in Docker containers, which are managed using Docker Swarm. The project uses a variety of DevOps tools such as Azure, and AWS for building virtual machines, Terraform for infrastructure as code, Ansible for automation, Nagios for monitoring, and Jenkins for continuous integration and delivery. We will use Terraform to create the required infrastructure in Azure including the resources like virtual networks, subnets, security groups, and virtual machines

<b>About the Project</b>

This project focuses on implementing a Continuous Integration/Continuous Deployment (CI/CD) pipeline for a software development team. This project aims to automate the entire software development lifecycle, from code changes to deployment, while ensuring quality and reliability. The CI/CD pipeline consists of multiple stages, including building, testing, and deploying the application. We use modern tools and technologies such as Git, Jenkins, Docker, and Kubernetes to automate the pipeline in this project.
  The CI/CD pipeline will automate the application's build and deployment processes, ensuring that the most recent changes are smoothly integrated, tested, and deployed. Jenkins will be used as the continuous integration tool, automatically initiating builds, testing, and deploying changes anytime they are uploaded to the code repository. The source code is committed to the version control system GIT, and updates are automatically grabbed by Jenkins before being tested and deployed as a Docker Swarm container. Terraform will be used to automate the provisioning of the cloud infrastructure that will host the docker swarm cluster, while Ansible will be used to manage the life cycle of the docker containers that will operate in the docker swarm cluster.
  Clients will benefit from numerous aspects of the project, including faster and more reliable deployments, decreased human tasks, and increased application quality. As a result, implementing a CI/CD pipeline for the QR code generator and scanner application would increase the efficiency and reliability of the application development and deployment process dramatically. Another key feature that improves the end-user experience is high availability and fault tolerance.

<b>Pipeline Architecture</b>

![image](https://user-images.githubusercontent.com/108337342/235503768-391295bb-31bf-4e7a-badb-41d9e22bcc1c.png)


<b>Jenkins Build Stages</b>

![image](https://user-images.githubusercontent.com/108337342/236038311-6966d024-6604-477e-a897-3374dfec3d8e.png)


<b>Sample Image</b>

![image](https://user-images.githubusercontent.com/108337342/235503799-2b8a5ce4-8f50-446f-868b-5ba792054f0e.png)

![image](https://user-images.githubusercontent.com/108337342/235503912-4044323e-441f-4b19-b984-809339ec2ff4.png)



<b>Application deployment Demo</b>




https://user-images.githubusercontent.com/108337342/236060960-9e3d07d2-53ec-41da-a2ae-f89b965bbec8.mp4




<b>Refer the attached Documentation for more details</b>

