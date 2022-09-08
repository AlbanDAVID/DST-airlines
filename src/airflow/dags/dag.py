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
from mysql_check_cnx_tables import mysql_cnx_and_tables_check
from lufthansa_api_check_status import lufthansa_api_check_status
from airlabs_api_check_status import airlabs_api_check_status
from transform_and_inject_data import transform_and_inject_data
from s3_cnx_check import aws_S3_connection_test
from mongodb_cnx_check import mongodb_connection_test


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


# check airlabs api status
airlabs_api_check_status = PythonOperator(
    task_id='airlabs_api_check_status',
    python_callable=airlabs_api_check_status,
    dag=my_dag
    
)

# check lufthansa api status
lufthansa_api_check_status = PythonOperator(
    task_id='lufthansa_api_check_status',
    python_callable=lufthansa_api_check_status,
    dag=my_dag,
    trigger_rule='all_success'
)

# test connection s3 datalake

s3_cnx_check = PythonOperator(
    task_id='s3_cnx_check',
    python_callable=aws_S3_connection_test,
    dag=my_dag,
    trigger_rule='all_success'
)
   
# test connection mongodb
mongodb_cnx_check = PythonOperator(
    task_id='mongodb_cnx_check',
    python_callable=mongodb_connection_test,
    dag=my_dag,
    trigger_rule='all_success'
)

# test connection to mysql database and check if there is tables inside (if not, create them)
mysql_cnx_and_tables_check = PythonOperator(
    task_id='mysql_cnx_and_tables_check',
    python_callable=mysql_cnx_and_tables_check,
    dag=my_dag,
    trigger_rule='all_success'
)

"""
# transform_and_inject_data

transform_and_inject_data = PythonOperator(
    task_id='transform_and_inject_data',
    python_callable=transform_and_inject_data,
    dag=my_dag,
    trigger_rule='all_success'
)
"""

airlabs_api_check_status >> lufthansa_api_check_status >> s3_cnx_check >> mongodb_cnx_check >> mysql_cnx_and_tables_check