#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:29:24 2022

@author: houda
"""
import requests
import json
import os


class LufthansaStatic :
    '''
    Extract static data from Lufthansa API
    '''
    
    def __init__(self , factory):
        self.factory = factory
   
    base_url = 'https://api.lufthansa.com/v1/mds-references/'


    def get_airport_data_luf(self, iata_airport, write_json = False ):
        
        if iata_airport== 'ALL':
            url = self.base_url + 'airports'
        else:
            url = self.base_url+'airports/'+iata_airport
        
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_airport_data_luf" + "_" + iata_airport, api_response)
            
        return  api_response
    
    def get_aircraft_data_luf(self, aircraft_code='ALL', write_json = False):
     
        if aircraft_code == 'ALL':
            url = self.base_url + 'aircraft'
        else:
            url = self.base_url+'aircraft/'+aircraft_code
            
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_aircraft_data_luf" + "_" + aircraft_code, api_response)
        
        return api_response
    
    
    def get_airline_data_luf(self, iata_airline, write_json = False):
        
        if iata_airline == 'ALL':
            url = self.base_url + 'airlines'
        else:
            url = self.base_url+'airlines/'+iata_airline
        
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_airline_data_luf" + "_" + iata_airline, api_response)
            
        return api_response
        
    def get_countries_data_luf(self, country_code, write_json = False):
        
        if country_code == 'ALL':
            url = self.base_url + 'countries' 
        else:
            url = self.base_url+'countries/' + country_code
            
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_countries_data_luf" + "_" + country_code, api_response)
            
        return api_response
    
    
    def get_cities_data_luf(self, city_code, write_json = False):
        
        if city_code == 'ALL':
            url = self.base_url + 'cities' 
        else:
            url = self.base_url+'cities/' + city_code
        
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_cities_data_luf" + "_" + city_code, api_response)
            
        return api_response
    
    
    def get_nearest_airports_luf(self, lat, long, write_json = False):
       
        url = self.base_url+'airports/nearest/'+str(lat)+','+str(long)
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_nearest_airports_luf" + "_" + lat + "_" + long, api_response)
        return api_response
    

    
    def __export_json(self, filename, response):

        json_dir_name = "tmp_json"
        path = os.path.join(os.getcwd(), json_dir_name)
        mode = 0o755
        if not os.path.exists(json_dir_name):
            os.mkdir(path, mode)
        filename = path + '/' + filename  + ".json"
        print ("Writing file : " + filename)
        with open(filename, 'w') as f:
            json.dump(response, f)
        f.close()
        
class AirlabsStatic:
    '''
    Extract static data from Airlabs API
    '''
    def __init__(self, api_key):
        self.api_key = api_key
    base_url = 'http://airlabs.co/api/v9/'

    def get_airports_airlabs(self, write_json = False):
        
        url = self.base_url + 'airports' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("airports_airlabs", api_response.json())
            
        return api_response.json()
    
    def get_airlines_airlabs(self, write_json = False):
        
        url = self.base_url + 'airlines' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("airlines_airlabs", api_response.json())
            
        return api_response.json()
    
    def get_cities_airlabs(self, write_json = False):
        
        url = self.base_url + 'cities' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("cities_airlabs", api_response.json())
            
        return api_response.json()
    
    def get_countries_airlabs(self, write_json = False):
        
        url = self.base_url + 'countries' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("countries_airlabs", api_response.json())
            
        return api_response.json()
    
    def __export_json(self, filename, response):

        json_dir_name = "tmp_json"
        path = os.path.join(os.getcwd(), json_dir_name)
        mode = 0o755
        if not os.path.exists(json_dir_name):
            os.mkdir(path, mode)
        filename = path + '/' + filename  + ".json"
        print ("Writing file : " + filename)
        with open(filename, 'w') as f:
            json.dump(response, f)
        f.close()

class LufthansaVariable:
    '''
    Extract variable data from Lufthansa API
    '''
    def __init__(self , factory):
        self.factory = factory
    
    base_url = "https://api.lufthansa.com/"
    
    def get_flight_route(self, origin, destination, date, write_json = True):
        
        url = self.base_url + 'v1/operations/flightstatus/route/' + origin +'/'+ destination+'/' + date
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_flight_route_luf" + origin + "_" + destination + "_" + date, api_response)
        
        return api_response 
    
    def get_flight_by_flight_number(self, flight_number, date,  write_json = True):
        
        url = self.base_url + 'v1/operations/customerflightinformation/' + flight_number +'/' + date
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json("get_flight_by_flight_number_luf" + "_" + flight_number  + "_" + date, api_response)
        
        return self.factory.create_request(url)
    
    def pprint(self, response):
        print(json.dumps(response, indent=4, sort_keys=True))
    
    def get_flights(self, startDate, endDate, daysOfOperation,flightType ="", airlines = "LH", flightNumberRanges = "",  timeMode = "UTC", origin = "", destination = "" , aircraftTypes = "", write_json = False):
        
        url = self.base_url + "v1/flight-schedules/flightschedules"
        if (flightType != ""):
            url += "/" + flightType
        url += "?"

        url = url + "airlines=" + airlines
        
        if flightNumberRanges != "":
            url  = url + "&flightNumberRanges=" + flightNumberRanges
            
        url = url + "&startDate=" + startDate + "&endDate=" + endDate + \
        "&daysOfOperation=" + daysOfOperation + \
        "&timeMode=" + timeMode
        
        if  origin != "":
            "&origin=" + origin 
        if  destination != "":
            "&destination=" + destination
        if  aircraftTypes != "":
            "&aircraftTypes=" + aircraftTypes
            
        api_response = self.factory.create_request(url)
        
        if write_json and api_response  != "invalid request":
            self.__export_json(" get_flights_lufthansa" + "_" + startDate + "_" + endDate, api_response)
        
        
        return  api_response
    
    def __export_json(self, filename, response):
        
        json_dir_name = "tmp_json"
        path = os.path.join(os.getcwd(), json_dir_name)
        mode = 0o755
        if not os.path.exists(json_dir_name):
            os.mkdir(path, mode)
        filename = path + '/' + filename  + ".json"
        print ("Writing file : " + filename)
        with open(filename, 'w') as f:
            json.dump(response, f)
        f.close()

class DstRealTime:
    '''
    Extract real time data and delays from Airlabs API
    '''
    def __init__(self, api_key):
        self.api_key = api_key
    
    base_url = 'http://airlabs.co/api/v9/'
    
    def get_flights(self, write_json = False):
        url = self.base_url + 'flights' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("get_flights", api_response.json())
            
        return api_response.json()
    
    def get_delays(self, delay, type, iata, write_json = False):
        """
        Retourne les avions qui ont un retard d'au moins 30 minutes.
        Il est possible de visualiser le retard au départ de l'aéroport ou bien à son arrivée
    
        Parametres: 
            delay (string). Le retard en minutes (doit être supérieur à 30 minutes) Ex : 35 
            type (string). Le type d'information souhaitée (au départ ou bien à l'arrivée) Ex : 'arrivals ou 'departures'
            iata (sting). Le code iata de la compagnie aérienne. Ex : 'LH' si l'on soihaite avoir les ingos sur les delays de la compagnie Lufthansa
    
        Retourne:
            Les infos sur le retard mais également le terminal de départ et d'arrivée (+ autres infos...)
    
    
        
        """
        url = self.base_url + 'delays?delay=' + delay + '&type=' + type + '&airline_iata=' + iata + '&api_key=' + self.api_key
        api_response = requests.get(url)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("delays_airlabs", api_response.json())
            
        return api_response.json()
    
    
     
    def get_flights_by_airline_iata(self, airline_iata,  write_json = False):
      
        params = {
                    'api_key': self.api_key,
                    'airline_iata': airline_iata
                 }
        
        url = self.base_url + 'flights'
        api_response = requests.get(url, params)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("get_flights_by_airline_iata" + "_" + airline_iata, api_response.json())
            
        return api_response.json()
    
    def get_flight_by_flight_iata(self, flight_iata, write_json = False):
    
        params = {
                    'api_key': self.api_key,
                    'flight_iata': flight_iata
                 }
        
        url = self.base_url + 'flight'
        api_response = requests.get(url, params)
        
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("get_flights_by_filght_iata" + "_" + flight_iata, api_response.json())
            
        return api_response.json()   
    
    def get_delays_by_airline_iata(self, airline_iata,  write_json = False):
      
        params = {
                    'api_key': self.api_key,
                    'airline_iata': airline_iata
                 }
        
        url = self.base_url + 'delays'
        api_response = requests.get(url, params)
        
        if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
            self.__export_json("get_delays_by_airline_iata" + "_" + airline_iata, api_response.json())
            
        return api_response.json()
    
    def __export_json(self, filename, response):
        
        json_dir_name = "tmp_json"
        path = os.path.join(os.getcwd(), json_dir_name)
        mode = 0o755
        if not os.path.exists(json_dir_name):
            os.mkdir(path, mode)
        filename = path + '/' + filename  + ".json"
        print ("Writing file : " + filename)
        with open(filename, 'w') as f:
            json.dump(response, f)
        f.close()

       
class AirlabsVariable:
    '''
    Extract variable data from Airlabs API
    '''
    def __init__(self, api_key):
        self.api_key = api_key
    base_url = 'http://airlabs.co/api/v9/' 
       
    def get_fleets_airlabs(self,airline_iata, write_json = False):
       
       params = {
                   'api_key': self.api_key,
                   'airline_iata': airline_iata
                }
       
       url = self.base_url + 'fleets'
       api_response = requests.get(url, params)
       
       if write_json and (api_response.status_code == 200 or api_response.status_code == 201):
           self.__export_json("fleet_airlabs", api_response.json())
           
       return api_response.json()
       
       
    def __export_json(self, filename, response):
       
       json_dir_name = "tmp_json"
       path = os.path.join(os.getcwd(), json_dir_name)
       mode = 0o755
       if not os.path.exists(json_dir_name):
           os.mkdir(path, mode)
       filename = path + '/' + filename  + ".json"
       print ("Writing file : " + filename)
       with open(filename, 'w') as f:
           json.dump(response, f)
       f.close()

       
