# DST Dashboard on Docker

### Rationale
This readme serves as reference for the functionality of the dashboard linked to the DST Airlines project and runing on Docker.
Through this readme, we will see :
- How to lauch the docker-compose
- Understand the tests that are run before the launch of the dashboard
- How to access the dashboard
- How to connect to the database with static.py

## Summary
#### I - Usage : launch docker-compose
#### II - Tests before runing the dash
#### III - Acced to the dashboard
#### IV - How to connect to the database with static.py (TODO)

## I - Usage

Run the following command lines (on a linux system or use VM) in order to build images and run them
```
bash setup.sh
```

## II - Tests before runing the dash
Two tests are executed before the execution of the dash:
- Verify if the connection to the databse (mysql in aws) works fine (password, username and database's name are correct)
- Verify that fetching data to this database works fine

The test results are accessible in the file 'dash_docker_log.log'

## III - Acced to the dashboard

to acced to the dashboard, you have to connect to the adress at the address provided (in the terminal where the setup.sh command was launched)

## IV - How to connect to the database with static.py
All login credentials are to be filled in the static.py file

