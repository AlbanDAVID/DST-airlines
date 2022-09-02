#!/bin/bash

# copy static.py in appropriate folders (before build images)
$cmd cp static.py docker_images/aws_mysql
$cmd cp static.py docker_images/dst_dashboard

# build and run images
$cmd docker-compose build --no-cache
$cmd docker-compose run aws_mysql_testv1

cd docker_images/dst_dashboard
$cmd  docker image build . -t dst_dashboard_docker-dash_app_testv1:latest
$cmd docker run -p 8050:8050 dst_dashboard_docker-dash_app_testv1:latest

# remove static.py copied before (in the case where we would like to build news images and change static.py)
$cmd rm docker_images/aws_mysql/static.py
$cmd rm docker_images/dst_dashboard/static.py
