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



# QUERIES POUR API LUFTHANSA

class LufthansaQueries:

    """
    Cette classe comprend les variables de classes necessaires pour se connecter a l'api lufthansa. Ces variables de classe seront utilisee par n'importe quelle classe heritant de cette classe. Une methode permet egalement de renvoyer le résultat au format .json 

    """
    data = {'client_id': CLIENT_ID,
                 'client_secret': CLIENT_SECRET,
                 'grant_type': GRANT_TYPE
   }
    
    lufthansa = requests.post('https://api.lufthansa.com/v1/oauth/token', data=data)

    token = 'Bearer ' + lufthansa.json()['access_token'] 
    headers = { 'Authorization': token,
        'Accept': 'application/json',
    }


    
    def get_result(self):

        response = requests.get(self.url, headers=self.headers)
        print(response.json())


class getFlightInfoLuf(LufthansaQueries):
    """
   Retourne le resultat de l'API Lufthansa (info en temps reel sur le vol en fonction du numero de vol et de la date) pour le chemin suivant : v1/operations/customerflightinformation/{flightNumber}/{date} 


    Parametres : 
        flight_number (string). Ex : 'LH1290'
        date (string au format YYYY-MM-DD). Ex : '2022-07-21'

    Retourne:
        Reponse de la requpete au format .json
    """
    def __init__(self, flight_number, date):
        self.flight_number = flight_number
        self.date = date
        self.url = f'https://api.lufthansa.com/v1/operations/customerflightinformation/{self.flight_number}/{self.date}'



class getFlightInfoByRouteLuf(LufthansaQueries):
    """
    Retourne le resultat au format .json de l'API lufthansa (info en temps reel sur le vol en fonction du code IATA de l'aeroport de depart et d'arrivee ainsi que la date) (le chemin est le suivant : v1/operations/customerflightinformation/route/{origin}/{destination}/{date}) 
    
    Parametres : 
        origine_iata (string). Ex : 'FRA'
        destination_iata (string). Ex : 'JFK'
        date (string). Ex : '2022-07-21'

    """
    
    def __init__ (self, origine_iata, destination_iata, date):
       self.origine_iata = origine_iata
       self.destination_iata  = destination_iata
       self.date = date
       self.url = f'https://api.lufthansa.com/v1/operations/customerflightinformation/route/{self.origine_iata}/{self.destination_iata}/{self.date}'

