#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:29:24 2022

@author: houda
"""
import requests
import json

class DstStatic :
    
    def __init__(self , factory):
        self.factory = factory
   
    base_url = 'https://api.lufthansa.com/v1/mds-references/'


    def get_airport_data(self, iata_airport ):
        
        if iata_airport== 'ALL':
            url = self.base_url + 'airports'
        else:
            url = self.base_url+'airports/'+iata_airport
        return  self.factory.create_request(url)
    
    def get_aircraft_data(self, aircraft_code='ALL'):
     
        if aircraft_code == 'ALL':
            url = self.base_url + 'aircraft'
        else:
            url = self.base_url+'aircraft/'+aircraft_code
        return self.factory.create_request(url)
    
    
    def get_airline_data(self, iata_airline):
        
        if iata_airline == 'ALL':
            url = self.base_url + 'airlines'
        else:
            url = self.base_url+'airlines/'+iata_airline
        return self.factory.create_request(url)
        
    def get_countries_data(self, country_code):
        
        if country_code == 'ALL':
            url = self.base_url + 'countries' 
        else:
            url = self.base_url+'countries/' + country_code
        return self.factory.create_request(url)
    
    
    def get_cities_data(self, city_code):
        
        if city_code == 'ALL':
            url = self.base_url + 'cities' 
        else:
            url = self.base_url+'cities/' + city_code
        return self.factory.create_request(url)
    
    
    def get_nearest_airports(self, lat, long):
       
        url = self.base_url+'airports/nearest/'+str(lat)+','+str(long)
        return self.factory.create_request(url)

class DstVariable:
    
    def __init__(self , factory):
        self.factory = factory
    
    base_url = "https://api.lufthansa.com/"
    
    def get_flight_route(self, origin, destination, date):
        
        url = self.base_url + 'v1/operations/flightstatus/route/' + origin +'/'+ destination+'/' + date
        return self.factory.create_request(url)
    
    def get_flight_by_flight_number(self, flight_number, date):
        
        url = self.base_url + 'v1/operations/customerflightinformation/' + flight_number +'/' + date
        return self.factory.create_request(url)
    
    def pprint(self, response):
        print(json.dumps(response, indent=4, sort_keys=True))
    
    def get_flights(self, startDate, endDate, daysOfOperation,flightType ="", airlines = "LH", flightNumberRanges = "",  timeMode = "UTC", origin = "", destination = "" , aircraftTypes = ""):
        
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
        
        return self.factory.create_request(url)

class DstRealTime:
   
    def __init__(self, api_key):
        self.api_key = api_key
    base_url = 'http://airlabs.co/api/v9/'
    
    def get_flights(self):
        url = self.base_url + 'flights' + '?' + 'api_key' + '=' + self.api_key
        api_response = requests.get(url)
        
        return(api_response.json())

     
    def get_flights_by_airline_iata(self, airline_iata):
      
        params = {
                    'api_key': self.api_key,
                    'airline_iata': airline_iata
                 }
     
        url = self.base_url + 'flights'
        api_response = requests.get(url, params)
        return(api_response.json())
    
    def get_flight_by_flight_iata(self, flight_iata):

        params = {
                    'api_key': self.api_key,
                    'flight_iata': flight_iata
                 }
        
        url = self.base_url + 'flight'
        api_response = requests.get(url, params)
        return(api_response.json())    
    
    
    
    
    