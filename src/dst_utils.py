#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 23:45:27 2022

@author: houda
"""

import requests 

class Authentication: 
    
    def __init__(self, client_key, client_secret):
        self.client_key = client_key
        self.client_secret = client_secret        
        end_point = "https://api.lufthansa.com/v1/oauth/token"
        data = {'client_id': self.client_key, 'client_secret':self.client_secret , 
                'grant_type': 'client_credentials'}
        token_request = requests.post(end_point, data)
        token = token_request.json()['access_token']
        
        self.token = token 

    def get_header(self):
        
        return {'accept': 'application/json', 'Authorization':'Bearer ' +self.token}
   
        
        
class RequestFactory:
    
    def __init__(self ,headers):
        self.headers = headers

    def create_request(self, url):
    
        
        response = requests.get(url, headers=self.headers) 
        
        if response.status_code == 200 or response.status_code == 206:
            print(url + "::" + str(response.status_code))
            return response.json()
        else : 
            print(url + "xx" + str(response.status_code))
            return "invalid request"


