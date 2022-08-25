#!/bin/bash

$cmd cp static.py docker_images/aws_mysql
$cmd cp static.py docker_images/dst_dashboard

$cmd docker-compose build --no-cache
$cmd docker-compose run aws_mysql_testv1
$cmd docker-compose run dash_app_testv1

$cmd rm docker_images/aws_mysql/static.py
$cmd rm docker_images/dst_dashboard/static.py