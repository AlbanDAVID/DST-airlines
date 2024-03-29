## Summary
#### I - Airflow dag presentation
#### II - How to run airflow
#### III - Libraries (warning)

## I - Airflow dag
There is our graph airflow dag : 

![Alt Text](readme_assests/airflow_dag_graphv2.png)

- 1. airlabs_api_check_status : check the airlabs api status
- 2. lufthansa_api_check_status : check the lufthansa api status
- 3. s3_cnx_check : check connection to s3 datalake
- 4. mongodb_cnx_check : check connection to mongodb
- 5. my_sql_cnx_and_tables_check : check the connection to mysql database and create tables if they not exists
- 6. transform_and_inject_data : fetch data from api's, cleaning data processing and inject data into mysql database

Note : All these steps are runned whether the previous tasks were successful

## II - How to run airflow

Run the following command line :
```
docker-compose up
```

And go to http://0.0.0.0:8080 to acced the airflow dashboard. The name of the dag is : dst-airlines-dag

## III - Libraries (warning)
The necessary libraries are included (as pymysql) in the docker-compose.yaml.
Therefore, each new library included in the dag.py must be installed via the docker-compose.yaml 
