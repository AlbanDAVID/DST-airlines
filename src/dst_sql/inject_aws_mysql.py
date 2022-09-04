import pandas as pd
import numpy as np
import pymysql
import sys


#### Function to inject data into AIRCRAFT table ####


def inject_AIRCRAFT(df, name_database):


  """
    Allows to inject data (from a dataframe) into AIRCRAFT database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """

  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)
  
  # get column index from column name 
  columns = AIRCRAFT.columns
  

  # verify in dataframe isn't None and inject data
  if AIRCRAFT is not None:
    for row in range(len(AIRCRAFT)):
 

      inject = "INSERT INTO AIRCRAFT (hex, airline_icao, airline_iata, icao, iata, manufacturer) VALUES ('{hex}', '{airline_icao}', '{airline_iata}', '{icao}','{iata}','{manufacturer}')".format(hex = AIRCRAFT.iloc[row,columns.get_loc('hex')],  airline_icao = AIRCRAFT.iloc[row, columns.get_loc('airline_icao')], airline_iata = AIRCRAFT.iloc[row,columns.get_loc('airline_iata')], icao = AIRCRAFT.iloc[row,columns.get_loc('icao')], iata = AIRCRAFT.iloc[row,columns.get_loc('iata')],manufacturer = AIRCRAFT.iloc[row,columns.get_loc('manufacturer')])





      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()

  else:
    cursor.close()
    cnx.close()


#### Function to inject data into COUNTRIES table ####

def inject_COUNTRIES(df, name_database):

  """
    Allows to inject data (from a dataframe) into COUNTRIES database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """

  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)
  
  # get column index from column name 
  columns = COUNTRIES.columns

  # verify in dataframe isn't None and inject data
  if COUNTRIES is not None:
    for row in range(len(COUNTRIES)):
 

      inject = "INSERT INTO COUNTRIES (code, code3, name) VALUES ('{code}', '{code3}', '{name}')".format(code = COUNTRIES.iloc[row,columns.get_loc('code')],  code3 = COUNTRIES.iloc[row, columns.get_loc('code3')], name = COUNTRIES.iloc[row,columns.get_loc('name')])





      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()
    
  else:
    cursor.close()
    cnx.close()


#### Function to inject data into AIRPORTS table ####

def inject_AIRPORTS(df, name_database):

  """
    Allows to inject data (from a dataframe) into AIRPORTS database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """

  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)

  # get column index from column name 
  columns = AIRPORTS.columns

  # verify in dataframe isn't None and inject data 
  if AIRPORTS is not None:
    for row in range(len(AIRPORTS)):
 

      inject = "INSERT INTO AIRPORTS (iata_code, icao_code, name, country_code, lat, lng) VALUES ('{iata_code}', '{icao_code}', '{name}', '{country_code}',{lat},{lng})".format(iata_code = AIRPORTS.iloc[row,columns.get_loc('iata_code')],  icao_code = AIRPORTS.iloc[row, columns.get_loc('icao_code')], name = AIRPORTS.iloc[row,columns.get_loc('name')], country_code = AIRPORTS.iloc[row,columns.get_loc('country_code')], lat = AIRPORTS.iloc[row,columns.get_loc('lat')],lng = AIRPORTS.iloc[row,columns.get_loc('lng')])





      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()

  else:
    cursor.close()
    cnx.close()


#### Function to inject data into CITIES table ####

def inject_CITIES(df, name_database):


  """
    Allows to inject data (from a dataframe) into CITIES database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """

  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)

  # get column index from column name 
  columns = CITIES.columns

  # verify in dataframe isn't None and inject data 
  if CITIES is not None:
    for row in range(len(CITIES)):
 

      inject = "INSERT INTO CITIES (city_code, country_code, name, lat, lng) VALUES ('{city_code}', '{country_code}', '{name}', {lat}, {lng})".format(city_code = CITIES.iloc[row,columns.get_loc('city_code')],  country_code = CITIES.iloc[row, columns.get_loc('country_code')], name = CITIES.iloc[row,columns.get_loc('name')],lat = CITIES.iloc[row,columns.get_loc('lat')], lng = CITIES.iloc[row,columns.get_loc('lng')] )

      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()

  else:
    cursor.close()
    cnx.close()

#### Function to inject data into FLIGHTS_METRICS table ####

def inject_FLIGHTS_METRICS(df, name_database):


  """
    Allows to inject data (from a dataframe) into FLIGHTS_METRICS database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """

  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)

  # get column index from column name 
  columns = FLIGHTS_METRICS.columns

  # verify in dataframe isn't None and inject data 
  if FLIGHTS_METRICS is not None:
    for row in range(len(FLIGHTS_METRICS)):
 

      inject = "INSERT INTO FLIGHTS_METRICS (hex, flight_icao, flight_iata, lat, lng, alt, dir, speed, v_speed, date_retrieve, time_retrieve) VALUES ('{hex}', '{flight_icao}', '{flight_iata}', {lat},{lng},{alt}, {dir},{speed},{v_speed},'{date_retrieve}','{time_retrieve}')".format(hex = FLIGHTS_METRICS.iloc[row,columns.get_loc('hex')],  flight_icao = FLIGHTS_METRICS.iloc[row, columns.get_loc('flight_icao')], flight_iata = FLIGHTS_METRICS.iloc[row,columns.get_loc('flight_iata')], lat = FLIGHTS_METRICS.iloc[row,columns.get_loc('lat')], lng = FLIGHTS_METRICS.iloc[row,columns.get_loc('lng')],alt = FLIGHTS_METRICS.iloc[row,columns.get_loc('alt')], dir = FLIGHTS_METRICS.iloc[row,columns.get_loc('dir')], speed = FLIGHTS_METRICS.iloc[row,columns.get_loc('speed')], v_speed = FLIGHTS_METRICS.iloc[row,columns.get_loc('v_speed')], date_retrieve= str(FLIGHTS_METRICS.iloc[row,columns.get_loc('date_retrieve')]), time_retrieve= str(FLIGHTS_METRICS.iloc[row,columns.get_loc('time_retrieve')]))

      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()

  else:
    cursor.close()
    cnx.close()


#### Function to inject data into FLIGHTS_SUMMARY table ####


def inject_FLIGHTS_SUMMARY(df, name_database):


  """
    Allows to inject data (from a dataframe) into FLIGHTS_SUMMARY database. 
    This function will first check if the dataframe exists.
    It will also connect to the database in which we want to inject our data.

    Arguments:
        df (dataframe) : name of the dataframe. 
        name_database (sring) : name of the database in which we want to inject our data.
    
    Returns:
        If dataframe is not empty and the injection is successful  : nothing
        Otherwise : Error message
    
  """


  # connection to database (AWD RDS)

  cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
  cursor = cnx.cursor()
  use_db = "use {name}".format(name = name_database)
  cursor.execute(use_db)

  # get column index from column name 
  columns = FLIGHTS_SUMMARY.columns

  # verify in dataframe isn't None and inject data 
  if FLIGHTS_SUMMARY is not None:

    for row in range(len(FLIGHTS_SUMMARY)):
 

      inject = "INSERT INTO FLIGHTS_SUMMARY (hex, flight_icao, flight_iata, status_lufthansa, flag, dep_iata, arr_iata, schedule_date_deps, schedule_date_arrs, schedule_time_deps, schedule_time_arrs, actual_date_deps, actual_date_arrs, actual_time_deps, actual_time_arrs, date_retrieve, time_retrieve, terminal_names_dep, terminal_names_arr,gates_dep, gates_arr) VALUES ('{hex}', '{flight_icao}', '{flight_iata}', '{status_lufthansa}','{flag}','{dep_iata}','{arr_iata}','{schedule_date_deps}','{schedule_date_arrs}','{schedule_time_deps}','{schedule_time_arrs}','{actual_date_deps}','{actual_date_arrs}','{actual_time_deps}','{actual_time_arrs}','{date_retrieve}','{time_retrieve}', '{terminal_names_dep}', '{terminal_names_arr}', '{gates_dep}','{gates_arr}')".format(hex = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('hex')],  flight_icao = FLIGHTS_SUMMARY.iloc[row, columns.get_loc('flight_icao')], flight_iata = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('flight_iata')], status_lufthansa = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('status_lufthansa')], flag = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('flag')],dep_iata = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('dep_iata')],arr_iata = FLIGHTS_SUMMARY.iloc[row,columns.get_loc('arr_iata')],schedule_date_deps = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('schedule_date_deps')]),schedule_date_arrs = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('schedule_date_arrs')]),schedule_time_deps = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('schedule_time_deps')]),schedule_time_arrs = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('schedule_time_arrs')]),actual_date_deps = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('actual_date_deps')]),actual_date_arrs = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('actual_date_arrs')]),actual_time_deps = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('actual_time_deps')]), actual_time_arrs = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('actual_time_arrs')]), date_retrieve= str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('date_retrieve')]), time_retrieve = str(FLIGHTS_SUMMARY.iloc[row,columns.get_loc('time_retrieve')]), terminal_names_dep = FLIGHTS_SUMMARY.iloc[row, columns.get_loc('terminal_names_dep')], terminal_names_arr = FLIGHTS_SUMMARY.iloc[row, columns.get_loc('terminal_names_arr')], gates_dep = FLIGHTS_SUMMARY.iloc[row, columns.get_loc('gates_dep')], gates_arr = FLIGHTS_SUMMARY.iloc[row, columns.get_loc('gates_arr')])

      cursor.execute(inject)

      cnx.commit()

    cursor.close()
    cnx.close()

  else:
    cursor.close()
    cnx.close()