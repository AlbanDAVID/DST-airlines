import requests
import pandas as pd
from collections import OrderedDict
import json

from sqlalchemy import create_engine
my_conn = create_engine("mysql+pymysql://admin:hyadeb22!@airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com/airlines5")

import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

from store_json_S3 import upload_file_airlabs
from read_file_from_s3 import read_latest_file

def get_rt_flights():
    api_flights = requests.get("https://airlabs.co/api/v9/flights?airline_iata=LH&api_key=4ae6f50c-89d1-48b6-b7d9-80133df2745d")
    api_flights_response = api_flights.json()
    if len(api_flights_response['response'])>0:
        with open('flights_airlabs.json', 'w') as f:
            json.dump(api_flights_response['response'], f)
            
        upload_file_airlabs("datalake-airlines", "01-real-time-flights-airlabs", "flights_airlabs", "flights_airlabs.json")
        data_flights = read_latest_file('datalake-airlines', '01-real-time-flights-airlabs/')
        db = client['data_airlines']
        col_flights = db['airlabs_real_time_flights']
        col_flights.delete_many({})
        col_flights.insert_many(data_flights)
    
        return api_flights_response


def get_dataframe_flights(json_flights):
    api_flights_df = pd.DataFrame(json_flights['response'])
    api_flights_df = api_flights_df.dropna(subset=['hex']).reset_index(drop=True)
    api_flights_df['dep_iata'] = api_flights_df['dep_iata'].fillna('XXXX')
    api_flights_df['arr_iata'] = api_flights_df['arr_iata'].fillna('XXXX')
    return api_flights_df



def get_missing_airports(api_flights_df):
    aiports_dep_flights_value = api_flights_df['dep_iata'].unique().tolist()
    aiports_arr_flights_value = api_flights_df['arr_iata'].unique().tolist()
    aiports_dep_flights_value = tuple(aiports_dep_flights_value)
    aiports_arr_flights_value = tuple(aiports_arr_flights_value)
    
    df_airports_dep = pd.read_sql_query(sql ="SELECT iata_code from AIRPORTS WHERE iata_code in {code_airports}".format(code_airports=aiports_dep_flights_value),con = my_conn)
    df_airports_arr = pd.read_sql_query(sql ="SELECT iata_code from AIRPORTS WHERE iata_code in {code_airports}".format(code_airports=aiports_arr_flights_value),con = my_conn)
    list_missing_air_dep = list(set(aiports_dep_flights_value) - set(df_airports_dep['iata_code'].unique().tolist()))
    list_missing_air_arr = list(set(aiports_arr_flights_value) - set(df_airports_arr['iata_code'].unique().tolist()))
    list_missing_air = list_missing_air_dep + list_missing_air_arr
    list_missing_air = list(OrderedDict.fromkeys(list_missing_air))
    
    if len(list_missing_air) > 0 :
        url2=""
        for x in list_missing_air:
            url1 = x
            url2 = url2+"iata_code="+url1+"&"

        api_airports = requests.get("https://airlabs.co/api/v9/airports?"+url2+"api_key=4ae6f50c-89d1-48b6-b7d9-80133df2745d")
        api_airports_response = api_airports.json()
        iata_code_airport_from_api = [a_dict['iata_code'] for a_dict in api_airports_response['response']]
        list_missing_iata_code_after_api = list(set(list_missing_air) - set(iata_code_airport_from_api))
        if len(list_missing_air) > 0:
            with open('airports_airlabs.json', 'w') as f:
                json.dump(api_airports['response'], f)
            upload_file_airlabs("datalake-airlines", "03-static-data", "airports_airlabs", "airports_airlabs.json")
            data_airports = read_latest_file('datalake-airlines', '03-static-data/','airports')
            db = client['data_airlines']
            col_airports = db['airports']
            col_airports.delete_many({})
            col_airports.insert_many(data_airports)
    return list_missing_air
    

        
def get_missing_aircraft(api_flights_df):
    aircraft_flights_value = api_flights_df['hex'].unique().tolist()
    aircraft_flights_value = tuple(aircraft_flights_value)
    df_aircraft = pd.read_sql_query(sql ="SELECT hex from AIRCRAFT WHERE hex in {code_aircraft}".format(code_aircraft=aircraft_flights_value),con = my_conn)
    list_missing_hex = list(set(aircraft_flights_value) - set(df_aircraft['hex'].unique().tolist()))
    if len(list_missing_hex) > 0 :
        url2=""
        for x in list_missing_hex:
            url1 = x
            url2 = url2+"hex="+url1+"&"

        api_fleets = requests.get("https://airlabs.co/api/v9/fleets?"+url2+"api_key=4ae6f50c-89d1-48b6-b7d9-80133df2745d")
        api_fleets_response = api_fleets.json()

        hex_code_from_api = [a_dict['hex'] for a_dict in api_fleets_response['response']]
        list_missing_hex_code_after_api = list(set(list_missing_hex) - set(hex_code_from_api))
        print(list_missing_hex_code_after_api)
        api_fleets_response = api_fleets_response['response']
    
        for i in range (0,len(list_missing_hex_code_after_api)):
            val={"hex":"","airline_icao":"","airline_iata":"","icao":"","iata":""}
            val["hex"] = list_missing_hex_code_after_api[i]
            val["airline_icao"] = "To be defined"
            val["airline_iata"] = "To be defined"
            val["icao"] = "To be defined"
            val["iata"] = "To be defined"
            api_fleets_response.append(val)
        if len(api_fleets_response)>0:
            with open('fleet_airlabs.json', 'w') as f:
                json.dump(api_fleets_response, f)
            upload_file_airlabs("datalake-airlines", "02-fleets-airlabs", "fleet_airlabs", "fleet_airlabs.json")
            data_fleets = read_latest_file('datalake-airlines', '02-fleets-airlabs/')
            db = client['data_airlines']
            col_fleets = db['fleet']
            col_fleets.delete_many({})
            col_fleets.insert_many(data_fleets)
            
        return api_fleets_response