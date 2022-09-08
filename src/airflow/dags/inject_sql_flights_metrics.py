import pandas as pd
from sqlalchemy import create_engine
my_conn = create_engine("mysql+pymysql://admin:hyadeb22!@airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com/airlines5")
import pymysql

def inject_sql_flights_metrics(FLIGHTS_METRICS, name_database):
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