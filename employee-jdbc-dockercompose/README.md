# Create External-DNS for Springboot Application

Pre-requisites:
-------

  Installations:
      -	git
      -	Java
      -	Maven
      -	docker
  EKS Cluster

Attach below policy to Node Instance Role
-----------

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "route53:ListHostedZones",
                "route53:ListResourceRecordSets"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

Get Source Code from github:
---------------
	https://github.com/Naresh240/employee-jdbc.git
Build artifact by using below command:
----------------
	mvn clean install
Create docker image:
----------
	docker build -t employee-jdbc .
Docker login:
-----------
We need to login before push image to docker hub
	docker login 
Tag docker image:
--------
	docker tag employee-jdbc naresh240/employee-jdbc
push docker image to docker hub:
---------
	docker push naresh240/employee-jdbc
Creating the secrets:
---------
You can create secrets manually from a literal or file using the kubectl create secret command, or you can create them from a generator using Kustomize.
In this article, we’re gonna create the secrets manually:

	kubectl create secret generic mysql-root-pass --from-literal=password=Naresh#240
	kubectl create secret generic mysql-user-pass --from-literal=username=naresh --from-literal=password=Naresh#240
	kubectl create secret generic mysql-db-url --from-literal=database=mysqldb --from-literal=url='jdbc:mysql://employee-jdbc-mysql:3306/mysqldb'
You can check the secrets:
------------
	kubectl get secrets
	kubectl describe secrets mysql-user-pass
Deploying MySQL & PV:
-----------
	kubectl apply -f mysql-service.yml
	kubectl apply -f mysql-deployment.yml
	kubectl apply -f mysql-pv.yml
	kubectl apply -f mysql-pv-claim.yml
To check Persistent volumes and Persistentvolumeclaim:
--------------
	kubectl get persistentvolumes
	kubectl get persistentvolumeclaims
Logging into the MySQL pod:
--------------
You can get the MySQL pod and use kubectl exec command to login to the Pod.

	kubectl get pods
	kubectl exec -it employee-jdbc-mysql-74d88fd675-cbnbf -- /bin/bash
Login in to mysql:

	mysql -u naresh -p
Change database to mysqldb:

	use mysqldb;
Create table with the name of employee:

	create table employee(empId varchar(40), empName varchar(40));
Now exit from pod:

	exit
Deploying the Spring Boot app on Kubernetes:
----------------
	kubectl apply -f employee-jdbc-deployment.yml
	kubectl apply -f employee-jdbc-service.yml
Deploying mandatory files for 
----------
	kubectl apply -f mandatory.yaml
	kubectl apply -f patch-configmap-l4.yaml
Create Certificates:
-------------
Create Certificates for our external-dns using AWS Certificate Manager

Deploying externaldns, service and ingress:
----------
change our external dns in below yml files and certificate arn

	kubectl apply -f external-dns.yaml
	kubectl apply -f service-l4.yaml
	kubectl apply -f ingress.yml
Check output with External-dns with API:
----------------
	employee.naresh.com/employees


