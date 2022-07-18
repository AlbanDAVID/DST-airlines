import requests
import json
from static import *

class getFlightAirlabs:
    def __init__(self, flight_iata):
        self.flight_iata = flight_iata 
        self.params = {
                  'api_key': API_KEY,
                   'flight_iata': self.flight_iata
                }
        self.method = 'flight'
        self.api_base = 'http://airlabs.co/api/v9/'
        self.api_result = requests.get(self.api_base+self.method, self.params)
        self.api_response = self.api_result.json()

    def print_request(self):
        print(json.dumps(self.api_response, indent=4, sort_keys=True))


