import requests
import json
from static import *



# QUERIES POUR API AIRLABS

class getFlightAirlabs:

    """
    Cette classe permet de se connecter a l'api airlbas et de sortir, en entrant le numero de voln les infos en temps reel, au format .json, du chemin suivant : https://airlabs.co/api/v9/flights?api_key=YOUR-API-KEY

    Parametres :
        flight_iata (string). Ex : 'LH1290'

    Retourne:
        Les donnees en temps reel au format .json
    """
    def __init__(self, flight_iata):
        self.flight_iata = flight_iata 
        self.params = {
                  'api_key': API_KEY,
                   'flight_iata': self.flight_iata
                }
        self.method = 'flight'
        self.api_base = 'http://airlabs.co/api/v9/'
        self.api_result = requests.get(self.api_base+self.method, self.params)
        self.api_response = self.api_result.json()['response']

    def print_request(self):
        return(json.dumps(self.api_response, indent=4, sort_keys=True))

