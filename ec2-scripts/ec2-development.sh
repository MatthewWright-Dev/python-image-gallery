#!/usr/bin/bash

#Install Packages
yum -y update
yum install -y nano python3 postgresql
yum install -y tree
yum install -y git
yum install -y gcc
yum install -y python3-devel
yum install -y postgresql-devel
amazon-linux-extras install -y nginx1
yum install -y docker

#Configure/install custom software
cd /home/ec2-user
git clone https://github.com/MatthewWright-Dev/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"


#Start and enable services
systemctl stop postfix
systemctl disable postfix
