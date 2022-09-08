import pandas as pd
from sqlalchemy import create_engine
my_conn = create_engine("mysql+pymysql://admin:hyadeb22!@airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com/airlines5")
import pymysql

def inject_AIRCRAFT(AIRCRAFT, name_database):
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