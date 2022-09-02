import pymysql
import sys
from pymysql import OperationalError
import pandas as pd
import numpy as np
import os
from datetime import datetime


# Connection test (password and username verification)

def aws_connection():
    try:
        cnx = pymysql.connect(host = 'airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com', user = "admin", password = "hyadeb22!")
        connection = "Successful connection"
    except OperationalError:
        connection = "Failed connection. Try another username/password"
    
    return connection

aws_connection()


# fetch data 

def fetch_data_aws():
    try:
        # pour faire des requêtes sql

        # connexion à la BDD

        name_database = 'airlines5'
        cnx = pymysql.connect(host = 'airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com', user = "admin", password = "hyadeb22!")
        cursor = cnx.cursor()
        use_db = "use {name}".format(name = name_database)
        cursor.execute(use_db)

        #### Execute query ####

        query1 = ("(SELECT * from FLIGHTS_SUMMARY LEFT JOIN AIRCRAFT ON FLIGHTS_SUMMARY.hex = AIRCRAFT.hex LEFT JOIN FLIGHTS_METRICS ON AIRCRAFT.hex = FLIGHTS_METRICS.hex LEFT JOIN AIRPORTS a ON FLIGHTS_SUMMARY.dep_iata = a.iata_code  LEFT JOIN AIRPORTS b ON FLIGHTS_SUMMARY.arr_iata = b.iata_code LEFT JOIN COUNTRIES as c ON a.country_code = c.code LEFT JOIN COUNTRIES as d ON b.country_code = d.code)")
        cursor.execute(query1)




        #### Create dataframe from resultant table ####
        frame = pd.DataFrame(cursor.fetchall())

        frame

        fetch_result = 'successful data fetching'

    
    except NameError:

        fetch_result = "Impossible to fetch data"

    return fetch_result


fetch_data_aws()