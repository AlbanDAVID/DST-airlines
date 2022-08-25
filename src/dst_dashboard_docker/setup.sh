#!/bin/bash

$cmd docker-compose build --no-cache


$cmd docker-compose run aws_mysql_testv1
$cmd docker-compose run dash_app_testv1
