import pandas as pd
from datetime import datetime
import numpy as np
from tqdm import tqdm
import time

import boto3
s3_client = boto3.client('s3', aws_access_key_id='AKIAUBEGQUNAZW3YUCNW' , aws_secret_access_key='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')

import certifi
from pymongo import MongoClient
ca = certifi.where()
client = MongoClient("mongodb+srv://user01:wpvPnKP2gdPW8inB@cluster0.tyo5f.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

import requests as r

from sqlalchemy import create_engine
my_conn = create_engine("mysql+pymysql://admin:hyadeb22!@airlines.cwpriwycnk6a.eu-west-2.rds.amazonaws.com/airlines5")

def get_flights_preprocessed():
    db = client['data_airlines']
    col_flights = db['airlabs_real_time_flights']
    df_flights = pd.DataFrame(list(col_flights.find()))
    df_flights=df_flights.dropna(subset=["flight_icao"]).reset_index(drop=True)
    df_flights['flight_iata'] = df_flights['flight_icao'].apply(lambda x : x[1:])
    df_flights=df_flights.dropna(subset=["flight_iata"]).reset_index(drop=True)

    client_key = "exzk4xtp9pr3txzssb2zqqd4"
    client_secret = "PfMrRRe6AyyB4kTJWdSx"
    end_point = "https://api.lufthansa.com/v1/oauth/token"
    data = {'client_id': client_key, 'client_secret':client_secret , 'grant_type': 'client_credentials'}
    token_request = r.post(end_point, data)
    token = token_request.json()['access_token']
    headers = {'Accept': 'application/json', 'Authorization':'Bearer ' +token}
    base_url = "https://api.lufthansa.com/"

    now = datetime.now()
    dt_string_date = now.strftime("%Y-%m-%d")
    date = dt_string_date
    flight_iata_errors = []

    aiport_deps=[]
    aiport_arrs=[]

    schedule_date_deps=[]
    schedule_date_arrs=[]
    schedule_time_deps=[]
    schedule_time_arrs=[]

    actual_date_deps=[]
    actual_date_arrs=[]
    actual_time_deps=[]
    actual_time_arrs=[]

    status=[]

    terminal_names_dep=[]
    gates_dep=[]
    terminal_names_arr=[]
    gates_arr=[]

    for i in tqdm(range (0,len(df_flights['flight_iata']))):
        time.sleep(1.3)
        val = df_flights['flight_iata'][i]
        print(val)
        url = base_url + "v1/operations/customerflightinformation/"+val+"/"+date
        
        try:
            schedule = r.get(url, headers=headers)
            api_flight_info_sup = schedule.json()
            if type(api_flight_info_sup['FlightInformation']['Flights']['Flight']) == dict :
                if api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Status']['Code'] != 'LD':
                    aiport_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['AirportCode']
                    aiport_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['AirportCode']
                    schedule_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Scheduled']['Date']
                    schedule_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Scheduled']['Date']
                    schedule_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Scheduled']['Time']
                    schedule_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Scheduled']['Time']
                    actual_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Actual']['Date']
                    actual_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Actual']['Date']
                    actual_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Actual']['Time']
                    actual_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Actual']['Time']
                    status_val = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Status']['Description']
                    try:
                        if len(api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']) == 2:
                            terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Name']
                            gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Gate']
                        else:
                            try:
                                terminal_name_dep = ""
                                gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Gate']
                            except:
                                terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Name']
                                gate_dep = ""
                    except:
                        gate_dep = ""
                        terminal_name_dep = ""
                        
                    try:
                        if len(api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']) == 2:
                            terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Name']
                            gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Gate']
                        else:
                            try:
                                terminal_name_arr = ""
                                gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Gate']
                            except:
                                terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Name']
                                gate_arr = ""
                    except:
                        gate_arr = ""
                        terminal_name_arr = ""
            
                else:
                    aiport_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['AirportCode']
                    aiport_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['AirportCode']
                    schedule_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Scheduled']['Date']
                    schedule_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Scheduled']['Date']
                    schedule_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Scheduled']['Time']
                    schedule_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Scheduled']['Time']
                    actual_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Actual']['Date']
                    actual_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Actual']['Date']
                    actual_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Actual']['Time']
                    actual_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Actual']['Time']
                    status_val = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Status']['Description']
                    try:
                        if len(api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']) == 2:
                            terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Name']
                            gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Gate']
                        else:
                            try:
                                terminal_name_dep = ""
                                gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Gate']
                            except:
                                terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Departure']['Terminal']['Name']
                                gate_dep = ""
                    except:
                        gate_dep = ""
                        terminal_name_dep = ""
                        
                    try:
                        if len(api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']) == 2:
                            terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Name']
                            gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Gate']
                        else:
                            try:
                                terminal_name_arr = ""
                                gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Gate']
                            except:
                                terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight']['Arrival']['Terminal']['Name']
                                gate_arr = ""
                    except:
                        gate_arr = ""
                        terminal_name_arr = ""
                    
            elif type(api_flight_info_sup['FlightInformation']['Flights']['Flight']) == list :
                for i in range(0,len(api_flight_info_sup['FlightInformation']['Flights']['Flight'])):
                    if api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Status']['Code'] != 'LD':
                        aiport_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['AirportCode']
                        aiport_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['AirportCode']
                        schedule_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Scheduled']['Date']
                        schedule_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Scheduled']['Date']
                        schedule_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Scheduled']['Time']
                        schedule_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Scheduled']['Time']
                        actual_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Actual']['Date']
                        actual_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Actual']['Date']
                        actual_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Actual']['Time']
                        actual_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Actual']['Time']
                        status_val = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Status']['Description']
                        try:
                            if len(api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']) == 2:
                                terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Name']
                                gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Gate']
                            else:
                                try:
                                    terminal_name_dep = ""
                                    gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Gate']
                                except:
                                    terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Name']
                                    gate_dep = ""
                        except:
                            gate_dep = ""
                            terminal_name_dep = ""
                
                        try:
                            if len(api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']) == 2:
                                terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Name']
                                gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Gate']
                            else:
                                try:
                                    terminal_name_arr = ""
                                    gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Gate']
                                except:
                                    terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Name']
                                    gate_arr = ""
                        except:
                            gate_arr = ""
                            terminal_name_arr = ""
                
                    else:
                        aiport_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['AirportCode']
                        aiport_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['AirportCode']
                        schedule_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Scheduled']['Date']
                        schedule_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Scheduled']['Date']
                        schedule_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Scheduled']['Time']
                        schedule_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Scheduled']['Time']
                        actual_date_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Actual']['Date']
                        actual_date_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Actual']['Date']
                        actual_time_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Actual']['Time']
                        actual_time_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Actual']['Time']
                        status_val = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Status']['Description']
                        try:
                            if len(api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']) == 2:
                                terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Name']
                                gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Gate']
                            else:
                                try:
                                    terminal_name_dep = ""
                                    gate_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Gate']
                                except:
                                    terminal_name_dep = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Departure']['Terminal']['Name']
                                    gate_dep = ""
                        except:
                            gate_dep = ""
                            terminal_name_dep = ""
                
                        try:
                            if len(api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']) == 2:
                                terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Name']
                                gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Gate']
                            else:
                                try:
                                    terminal_name_arr = ""
                                    gate_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Gate']
                                except:
                                    terminal_name_arr = api_flight_info_sup['FlightInformation']['Flights']['Flight'][i]['Arrival']['Terminal']['Name']
                                    gate_arr = ""
                        except:
                            gate_arr = ""
                            terminal_name_arr = ""
        except:
            aiport_dep = np.nan
            aiport_arr = np.nan
            schedule_date_dep =np.nan
            schedule_date_arr =np.nan
            schedule_time_dep =np.nan
            schedule_time_arr =np.nan
            actual_date_dep = np.nan
            actual_date_arr = np.nan
            actual_time_dep = np.nan
            actual_time_arr = np.nan
            status_val = np.nan
            terminal_name_dep =np.nan
            terminal_name_arr =np.nan
            gate_dep = np.nan
            gate_arr = np.nan
        
        aiport_deps.append(aiport_dep)
        aiport_arrs.append(aiport_arr)
        schedule_date_deps.append(schedule_date_dep)
        schedule_date_arrs.append(schedule_date_arr)
        schedule_time_deps.append(schedule_time_dep)
        schedule_time_arrs.append(schedule_time_arr)
        actual_date_deps.append(actual_date_dep)
        actual_date_arrs.append(actual_date_arr)
        actual_time_deps.append(actual_time_dep)
        actual_time_arrs.append(actual_time_arr)
        status.append(status_val)
        terminal_names_dep.append(str(terminal_name_dep))
        gates_dep.append(str(gate_dep))
        terminal_names_arr.append(str(terminal_name_arr))
        gates_arr.append(str(gate_arr))

    df_flights['aiport_deps'] = aiport_deps
    df_flights['aiport_arrs'] = aiport_arrs
    df_flights['schedule_date_deps'] = schedule_date_deps
    df_flights['schedule_date_arrs'] = schedule_date_arrs
    df_flights['schedule_time_deps'] = schedule_time_deps
    df_flights['schedule_time_arrs'] = schedule_time_arrs
    df_flights['actual_date_deps'] = actual_date_deps
    df_flights['actual_date_arrs'] = actual_date_arrs
    df_flights['actual_time_deps'] = actual_time_deps
    df_flights['actual_time_arrs'] = actual_time_arrs
    df_flights['status_lufthansa'] = status
    df_flights['terminal_names_dep'] = terminal_names_dep
    df_flights['gates_dep'] = gates_dep
    df_flights['terminal_names_arr'] = terminal_names_arr
    df_flights['gates_arr'] = gates_arr

    dt_string_date = now.strftime("%Y-%m-%d")
    dt_string_time = now.strftime("%H:%M")
    df_flights['date_retrieve'] = dt_string_date
    df_flights['time_retrieve'] = dt_string_time
    
    df_flights['arr_iata']=df_flights['arr_iata'].fillna("XXXX")
    df_flights['dep_iata']=df_flights['dep_iata'].fillna("XXXX")
    df_flights[['reg_number', 'flag','squawk', 'flight_number', 'flight_icao', 'dep_icao', 'dep_iata',
            'arr_icao', 'arr_iata', 'airline_icao', 'airline_iata', 'aircraft_icao',
            'updated', 'status', 'flight_iata', 'aiport_deps', 'aiport_arrs', 'status_lufthansa',
            'terminal_names_dep', 'gates_dep', 'terminal_names_arr', 'gates_arr']] = df_flights[['reg_number', 'flag','squawk', 'flight_number', 'flight_icao', 'dep_icao', 'dep_iata',
                                                                                                    'arr_icao', 'arr_iata', 'airline_icao', 'airline_iata', 'aircraft_icao',
                                                                                                    'updated', 'status', 'flight_iata', 'aiport_deps', 'aiport_arrs', 'status_lufthansa',
                                                                                                    'terminal_names_dep', 'gates_dep', 'terminal_names_arr', 'gates_arr']].fillna("To be defined")
    df_flights[['schedule_date_deps', 'schedule_date_arrs','actual_date_deps', 'actual_date_arrs']]=df_flights[['schedule_date_deps', 'schedule_date_arrs','actual_date_deps', 'actual_date_arrs']].fillna("1900-01-01")
    df_flights[['schedule_time_deps','schedule_time_arrs','actual_time_deps', 'actual_time_arrs']]=df_flights[['schedule_time_deps','schedule_time_arrs','actual_time_deps', 'actual_time_arrs']].fillna("00:01")
    df_flights['terminal_names_dep'] = df_flights['terminal_names_dep'].apply(lambda x:x.replace('nan','no terminal'))
    df_flights['terminal_names_arr'] = df_flights['terminal_names_arr'].apply(lambda x:x.replace('nan','no terminal'))
    df_flights[['lat', 'lng', 'alt', 'dir', 'speed']]=df_flights[['lat', 'lng', 'alt', 'dir', 'speed']].fillna(-1.0)
    return df_flights