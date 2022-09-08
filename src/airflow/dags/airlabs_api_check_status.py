
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
  
    if str(api_result) == '<Response [200]>':
        print('Succes connection to airlabs API : {api_result}'.format(api_result = api_result))
    elif str(api_result) != '<Response [200]>':
        raise Exception('Error : {api_result}'. format(api_result = api_result))

airlabs_api_check_status()