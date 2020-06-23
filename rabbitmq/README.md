# RabbitMq deployment with Docker

Pre-requisites:
-------------
    - Install Java
    - Install Git
    - Install Maven
    - Install Docker
Install Java:
--------
    yum install java-1.8.0-openjdk-devel -y
Install Git:
------
    yum install git -y
Install Apache-Maven:
------
    wget https://mirrors.estointernet.in/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
    tar xvzf apache-maven-3.6.3-bin.tar.gz

    vi /etc/profile.d/maven.sh
    --------------------------------------------
    export MAVEN_HOME=/opt/apache-maven-3.6.3
    export PATH=$PATH:$MAVEN_HOME/bin
    --------------------------------------------

    source /etc/profile.d/maven.sh
    mvn -version
Install Docker:
---------
    yum install docker -y
    service docker start
Clone SCM form github:
---------
    git clone https://github.com/Naresh240/docker.git
    cd docker/rabbitmq/
Build Docker Image:
--------
    docker build -t naresh240/rabbitmq:latest .
Login to DockerHub:
----------
    docker login 
Run Docker Image:
-----------
    docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 -d naresh240/rabbitmq:latest
Check With Producer sending data or not:
-----------
    cd producer-SpringBootRabbitMQHelloWorld
    mvn springboot:run
Goto UI and send data using below link:
-----------
    http://<ip address>:8080/javainuse-rabbitmq/producer?empName=emp1&empId=emp001
