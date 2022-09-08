import pandas as pd
from sqlalchemy import create_engine
my_conn = create_engine("mysql+pymysql://admin:hyadeb22!@airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com/airlines5")
import pymysql


def inject_sql_flights_summary(FLIGHTS_SUMMARY, name_database):
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