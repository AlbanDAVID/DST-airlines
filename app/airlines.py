import requests



data = {
    'client_id': 'bnagmhp63tmy78hfpa3v2bgw',
    'client_secret': 'MVZHkTAMqc4y4Esz2ye5',
    'grant_type': 'client_credentials'
}

lufthansa = requests.post('https://api.lufthansa.com/v1/oauth/token', data=data)

token = 'Bearer ' + lufthansa.json()['access_token']

headers = {
    'Authorization': token,
    'Accept': 'application/json',
}

response = requests.get('https://api.lufthansa.com/v1/flightschedules/passenger', headers=headers)


print(response.json())

