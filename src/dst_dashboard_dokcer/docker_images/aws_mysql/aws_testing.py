import pymysql
import sys
from pymysql import OperationalError
import pandas as pd
import numpy as np
import os
from datetime import datetime
import static

# date and time during request
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Connection test (password and username verification)

try:
    cnx = pymysql.connect(host = static.host, user = static.user, password = static.password)
    connection = "Successful connection"
except OperationalError:
    connection = "Failed connection. Try another username/password"



output = '''
==========================================================
    Connection test (password and username verification)
    {date_time}
==========================================================

| username="admin"
| password="XXXXX"

expected result = Successful connection
actual restult = {connection}

'''

print(output.format(date_time=dt_string, connection=connection))
output = output.format(date_time=dt_string, connection=connection)

# print output in a file

with open('/home/log/dash_docker_log.log', 'a') as file:
    file.write(output)


# fetch data 

try:
    # pour faire des requêtes sql

    # connexion à la BDD

    name_database = 'airlines5'
    cnx = pymysql.connect(host = static.host, user = static.user, password = static.password)
    cursor = cnx.cursor()
    use_db = "use {name}".format(name = name_database)
    cursor.execute(use_db)

    #### Execute query ####

    query1 = ("(SELECT * from FLIGHTS_SUMMARY LEFT JOIN AIRCRAFT ON FLIGHTS_SUMMARY.hex = AIRCRAFT.hex LEFT JOIN FLIGHTS_METRICS ON AIRCRAFT.hex = FLIGHTS_METRICS.hex LEFT JOIN AIRPORTS a ON FLIGHTS_SUMMARY.dep_iata = a.iata_code  LEFT JOIN AIRPORTS b ON FLIGHTS_SUMMARY.arr_iata = b.iata_code LEFT JOIN COUNTRIES as c ON a.country_code = c.code LEFT JOIN COUNTRIES as d ON b.country_code = d.code)")
    cursor.execute(query1)




    #### Create dataframe from resultant table ####
    frame = pd.DataFrame(cursor.fetchall())

    frame

    connection = 'successful data fetching'

    
except NameError:

    connection = "Impossible to fetch data"


output = '''
==========================================================
    fetch data
    {date_time}
==========================================================


expected result = successful data fetching
actual restult = {connection}

'''

print(output.format(date_time=dt_string, connection=connection))
output = output.format(date_time=dt_string, connection=connection)

# print output in a file

with open('/home/log/dash_docker_log.log', 'a') as file:
    file.write(output)



