#!/bin/bash

# copy static.py in appropriate folders (before build images)
$cmd cp static.py docker_images/aws_mysql
$cmd cp static.py docker_images/dst_dashboard

# build and run images
$cmd docker-compose build --no-cache
$cmd docker-compose run aws_mysql_testv1
$cmd docker-compose run dash_app_testv1

# remove static.py copied before (in the case where we would like to build news images and change static.py)
$cmd rm docker_images/aws_mysql/static.py
$cmd rm docker_images/dst_dashboard/static.py
