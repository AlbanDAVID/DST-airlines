#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 09:29:24 2022

@author: houda
"""



class DstStatic :
    
    def __init__(self , factory):
        self.factory = factory
   
    base_url = 'https://api.lufthansa.com/v1/mds-references/'


    def get_airport_data(self, iata_airport ):
        
        url = self.base_url+'airports/'+iata_airport
        return  self.factory.create_request(url)
    
    
    def get_aircraft_data(self, aircraft_code='ALL'):
     
        if aircraft_code == 'ALL':
            url = self.base_url + 'aircraft/'
        else:
            url = self.base_url+'aircraft/'+aircraft_code
        return self.factory.create_request(url)
    
    
    def get_airline_data(self, iata_airline):
        
        if iata_airline == 'ALL':
            url = self.base_url + 'airlines/'
        else:
            url = self.base_url+'airlines/'+iata_airline
            return self.factory.create_request(url)
        
    def get_countries_data(self, country_code):
        
        if country_code == 'ALL':
            url = self.base_url + 'countries/' 
        else:
            url = self.base_url+'countries/' + country_code
            return self.factory.create_request(url)
    
    
    def get_cities_data(self, city_code):
        
        if city_code == 'ALL':
            url = self.base_url + 'cities/' 
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
        

    
    
    
    
    
    
    
    
    
    
    
    
    