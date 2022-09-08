import requests
import static

def lufthansa_api_check_status():
    data = {
        'client_id': static.client_id_luf,
        'client_secret': static.client_secret_luf,
        'grant_type': 'client_credentials'
    }

    lufthansa = requests.post('https://api.lufthansa.com/v1/oauth/token', data=data)

    token = 'Bearer ' + lufthansa.json()['access_token']

    headers = {
        'Authorization': token,
        'Accept': 'application/json',
    }

    response = requests.get('https://api.lufthansa.com/v1/mds-references/aircraft', headers=headers)

    if str(response) == '<Response [200]>':
        print('Succes connection to Lufthansa API : {response}'.format(response = response))
    elif str(response) != '<Response [200]>':
        raise Exception('Error : {response}'. format(response = response))

lufthansa_api_check_status()