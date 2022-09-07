
import requests
import json
import static



def airlabs_api_check_status():
    params = {
        'api_key': static.api_key_airlabs,
        'flight_iata': 'LH2001'
        }
    method = 'flight'
    api_base = 'http://airlabs.co/api/v9/'
    api_result = requests.get(api_base+method, params)
  
    print(api_result)


airlabs_api_check_status()