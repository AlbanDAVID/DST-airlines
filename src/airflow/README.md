# DST Dashboard


## Summary
#### I - Airflow dag
#### II - How to run airflow

## I - Airflow dag
There is our graph airflow dag



- 1. my_sql_table_check : check the connection to mysql database and create tables if they not exists
- 2. s3_cnx_check : check connection to s3 datalake
- 3. mongodb_cnx_check : check connection to mongodb
- 4. lufthansa_api_check_status : check the lufthansa api status
- 5. airlabs_apo_check_status : check the airlabs api status
- 6. inject_data : fetch data from api's, cleaning data processing and inject data into mysql database

## II - How to run airflow

Run the following command line :
```
docker-compose up
```

And go to http://0.0.0.0:8080 to acced the airflow dashboard. The name of the dag is : dst-airlines-dag

