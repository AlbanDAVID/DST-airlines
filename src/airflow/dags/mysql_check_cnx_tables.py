import pymysql
import sys
from pymysql import OperationalError
import pandas as pd
import numpy as np
import os
from datetime import datetime
import static

# function to check if connexion to bdd is ok and id tables are created (if not, create them)

def mysql_cnx_and_tables_check():

    # connexion à la BDD

    name_database = static.name_bdd
    cnx = pymysql.connect(host = static.host, user = static.user, password = static.password)
    cursor = cnx.cursor()
    use_db = "use {name}".format(name = name_database)
    cursor.execute(use_db)

    #### Execute query ####

    query1 = ("show tables")
    cursor.execute(query1)


    #### Create dataframe from resultant table ####
    frame = pd.DataFrame(cursor.fetchall())


    # TJRS FERMER LA CONNEXION APR7S UNE REQUETE (SINON : Bug) !

    cursor.close()
    cnx.close()


    # check if table are created (this mysql db need 6 tables, so we check if 6 tables are present)
    if frame.shape[0] != 6:

        #### Create table AIRCRAFT ####

        create_AIRCRAFT = """

        CREATE TABLE AIRCRAFT (
        hex VARCHAR(30) NOT NULL,
        airline_icao VARCHAR(30),
        airline_iata VARCHAR(30),
        icao VARCHAR(30),
        iata VARCHAR(30),
        manufacturer VARCHAR(30),
        PRIMARY KEY (hex)
        );

        """

        cursor.execute(create_AIRCRAFT)



        #### Create table COUNTRIES ####

        create_COUNTRIES = """

        CREATE TABLE COUNTRIES (
        code VARCHAR(30) NOT NULL,
        code3 VARCHAR(30) NOT NULL,
        name VARCHAR(100),
        PRIMARY KEY (code, code3)
        );

        """

        cursor.execute(create_COUNTRIES)


        #### Create table AIRPORTS ####

        create_AIRPORTS = """

        CREATE TABLE AIRPORTS (
        iata_code VARCHAR(30) NOT NULL,
        icao_code VARCHAR(30),
        name VARCHAR(100),
        country_code VARCHAR(30),
        lat FLOAT,
        lng FLOAT,
        PRIMARY KEY (iata_code)
        );


        """

        cursor.execute(create_AIRPORTS)




        #### Create table CITIES ####

        create_CITIES = """

        CREATE TABLE CITIES (
        city_code VARCHAR(30) NOT NULL,
        country_code VARCHAR(30),
        name VARCHAR(100),
        lat FLOAT,
        lng FLOAT,
        PRIMARY KEY (city_code),
        FOREIGN KEY (country_code)
        REFERENCES COUNTRIES(code)
        );


        """

        cursor.execute(create_CITIES)


        #### Create table FLIGHTS_METRICS ####

        create_FLIGHTS_METRICS = """

        CREATE TABLE FLIGHTS_METRICS (
        id INT NOT NULL AUTO_INCREMENT,
        hex VARCHAR(30) NOT NULL,
        flight_icao VARCHAR(30),
        flight_iata VARCHAR(30),
        lat FLOAT,
        lng FLOAT,
        alt FLOAT,
        dir FLOAT,
        speed FLOAT,
        v_speed FLOAT,
        date_retrieve DATE,
        time_retrieve TIME,
        PRIMARY KEY (id),
        FOREIGN KEY (hex)
        REFERENCES AIRCRAFT(hex)
        );


        """

        cursor.execute(create_FLIGHTS_METRICS)


        #### Create table FLIGHTS_SUMMARY ####

        create_FLIGHTS_SUMMARY = """

        CREATE TABLE FLIGHTS_SUMMARY (
        id INT NOT NULL AUTO_INCREMENT,
        hex VARCHAR(30) NOT NULL,
        flight_icao VARCHAR(30),
        flight_iata VARCHAR(30),
        status_lufthansa VARCHAR(30),
        flag VARCHAR(30),
        dep_iata VARCHAR(30),
        arr_iata VARCHAR(30),
        schedule_date_deps DATE,
        schedule_date_arrs DATE,
        schedule_time_deps TIME,
        schedule_time_arrs TIME,
        actual_date_deps DATE,
        actual_date_arrs DATE,
        actual_time_deps TIME,
        actual_time_arrs TIME,
        date_retrieve DATE,
        time_retrieve TIME,
        terminal_names_dep VARCHAR(30),
        terminal_names_arr VARCHAR(30),
        gates_dep VARCHAR(30),
        gates_arr VARCHAR(30),
        PRIMARY KEY (id),
        FOREIGN KEY (hex)
        REFERENCES AIRCRAFT(hex),
        FOREIGN KEY (flag)
        REFERENCES COUNTRIES(code),
        FOREIGN KEY (dep_iata)
        REFERENCES AIRPORTS(iata_code),
        FOREIGN KEY (arr_iata)
        REFERENCES AIRPORTS(iata_code)

        );


        """

        cursor.execute(create_FLIGHTS_SUMMARY)

        print('table created and connection to mysql ok')

    else:
        print('tables already created and connection to mysql ok')

mysql_cnx_and_tables_check()