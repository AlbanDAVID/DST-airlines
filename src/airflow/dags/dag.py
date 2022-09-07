import requests
import json 
import time
import pymysql
import sys
from pymysql import OperationalError
import pandas as pd
import numpy as np
import os
from datetime import datetime
import static
from mysql_check_cnx_tables import mysql_tables_check
from lufthansa_api_check_status import lufthansa_api_check_status
from airlabs_api_check_status import airlabs_api_check_status
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

my_dag = DAG(
    dag_id='dst-airlines-dag',
    tags=['dst-airlines', 'datascientest'],
    schedule_interval=None,
    default_args={
        'owner': 'airflow',
        'start_date': days_ago(0, minute=1),
    }
)

# test connection to mysql database and check if there is tables inside (if not, create them)
mysql_tables_check = PythonOperator(
    task_id='mysql_tables_check',
    python_callable=mysql_tables_check,
    dag=my_dag
)

# test connection s3 datalake
def s3_cnx_check():
    print('successful connection to s3')

s3_cnx_check = PythonOperator(
    task_id='s3_cnx_check',
    python_callable=s3_cnx_check,
    dag=my_dag
)

# test connection mongodb
def mongodb_cnx_check():
    print('successful connection to mongodb')

mongodb_cnx_check = PythonOperator(
    task_id='mongodb_cnx_check',
    python_callable=mongodb_cnx_check,
    dag=my_dag
)

# check lufthansa api status
lufthansa_api_check_status = PythonOperator(
    task_id='lufthansa_api_check_status',
    python_callable=lufthansa_api_check_status,
    dag=my_dag
)


# check airlabs api status
airlabs_api_check_status = PythonOperator(
    task_id='airlabs_api_check_status',
    python_callable=airlabs_api_check_status,
    dag=my_dag
)

# inject_data
def inject_data():
    print('successful data injection')

inject_data = PythonOperator(
    task_id='inject_data',
    python_callable=inject_data,
    dag=my_dag
)


mysql_tables_check >> s3_cnx_check >> mongodb_cnx_check >> lufthansa_api_check_status >> airlabs_api_check_status >> inject_data