import pandas as pd
import pymysql


name_database = 'airlines5'
cnx = pymysql.connect(host = "airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com", user = "admin", password ="hyadeb22!")
cursor = cnx.cursor()
use_db = "use {name}".format(name = name_database)
cursor.execute(use_db)


# test jointure entre toutes les tables

#### Execute query ####

query_cities = ("(SELECT * from CITIES )")
query_countries = ("(SELECT * from COUNTRIES )")
query_aircraft = ("(SELECT * from AIRCRAFT )")
query_airports = ("(SELECT * from AIRPORTS)")
query_flights_metrics = ("(SELECT * from FLIGHTS_METRICS)")
query_flights_summary = ("(SELECT * from FLIGHTS_SUMMARY)")
query_summary_metrics = ("(SELECT * from FLIGHTS_SUMMARY LEFT JOIN FLIGHTS_METRICS ON FLIGHTS_SUMMARY.hex = FLIGHTS_METRICS.hex)")
query_summary_metrics_airports = ("(SELECT * from FLIGHTS_SUMMARY LEFT JOIN FLIGHTS_METRICS ON FLIGHTS_SUMMARY.hex = FLIGHTS_METRICS.hex LEFT JOIN AIRPORTS a ON FLIGHTS_SUMMARY.dep_iata = a.iata_code  LEFT JOIN AIRPORTS b ON FLIGHTS_SUMMARY.arr_iata = b.iata_code)")

cursor.execute(query_cities)
df_cities = pd.DataFrame(cursor.fetchall(), columns = ['city_code','country_code','city_name','city_lat','city_lng'])
cursor.execute(query_countries)
df_countries = pd.DataFrame(cursor.fetchall(), columns = ['country_code' ,'country_code3','name'])
cursor.execute(query_aircraft)
df_aircraft = pd.DataFrame(cursor.fetchall(), columns = ['hex','airline_icao','airline_iata','aircraft_icao','aircraft_iata','manufacturer'])
cursor.execute(query_airports)
df_airports = pd.DataFrame(cursor.fetchall(), columns = ['iata_code','icao_code' ,'airport_name','country_code','airport_lat','airport_lng'])
cursor.execute(query_flights_metrics)
df_flights_metrics= pd.DataFrame(cursor.fetchall(), columns = ['id','hex','flight_icao','flight_iata','lat' ,'lng','alt','dir','speed' ,'v_speed','date_retrieve','time_retrieve'])
cursor.execute(query_flights_summary)
df_flights_summary= pd.DataFrame(cursor.fetchall(), columns = ['id' , 'hex' ,'flight_icao' ,'flight_iata' ,'status_lufthansa' ,'flag' ,'dep_iata' ,'arr_iata' ,'schedule_date_deps' ,'schedule_date_arrs' ,'schedule_time_deps' ,'schedule_time_arrs','actual_date_deps' ,'actual_date_arrs','actual_time_deps' ,'actual_time_arrs' ,'date_retrieve' ,'time_retrieve' ,'terminal_names_dep' ,'terminal_names_arr' ,'gates_dep' ,'gates_arr'])
cursor.execute(query_summary_metrics)
df_summary_metrics= pd.DataFrame(cursor.fetchall())
df_summary_metrics= df_summary_metrics.drop(columns=[22, 23, 24, 25])
df_summary_metrics.columns =['id' ,
'hex' ,
'flight_icao' ,
'flight_iata' ,
'status_lufthansa' ,
'flag' ,
'dep_iata' ,
'arr_iata' ,
'schedule_date_deps' ,
'schedule_date_arrs' ,
'schedule_time_deps' ,
'schedule_time_arrs',
'actual_date_deps' ,
'actual_date_arrs',
'actual_time_deps' ,
'actual_time_arrs' ,
'date_retrieve' ,
'time_retrieve' ,
'terminal_names_dep' ,
'terminal_names_arr' ,
'gates_dep' ,
'gates_arr',
'lat' ,
'lng',
'alt',
'dir',
'speed' ,
'v_speed',
'date_retrieve',
'time_retrieve' ]





#### Create dataframe from resultant table ####
cursor.execute(query_summary_metrics_airports)
df_summary_metrics_airports = pd.DataFrame(cursor.fetchall())
df_summary_metrics_airports= df_summary_metrics_airports.drop(columns=[22, 23, 24, 25])
df_summary_metrics_airports.columns = ['id' ,
'hex' ,
'flight_icao' ,
'flight_iata' ,
'status_lufthansa' ,
'flag' ,
'dep_iata' ,
'arr_iata' ,
'schedule_date_deps' ,
'schedule_date_arrs' ,
'schedule_time_deps' ,
'schedule_time_arrs',
'actual_date_deps' ,
'actual_date_arrs',
'actual_time_deps' ,
'actual_time_arrs' ,
'date_retrieve' ,
'time_retrieve' ,
'terminal_names_dep' ,
'terminal_names_arr' ,
'gates_dep' ,
'gates_arr',
'lat' ,
'lng',
'alt',
'dir',
'speed' ,
'v_speed',
'date_retrieve',
'time_retrieve',
'dep_iata_code',
'dep_icao_code' ,
'dep_airport_name',
'dep_country_code',
'dep_airport_lat',
'dep_airport_lng',
#Airoports
'arr_iata_code',
'arr_icao_code' ,
'arr_airport_name',
'arr_country_code',
'arr_airport_lat',
'arr_airport_lng']
#### Create dataframe from resultant table ####
#pd.set_option("display.max_rows", None, "display.max_columns", None)

# TJRS FERMER LA CONNEXION APR7S UNE REQUETE (SINON : Bug) !

#cursor.close()
#cnx.close()



#frame