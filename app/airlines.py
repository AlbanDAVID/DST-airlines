import requests
from config.static import *

data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': GRANT_TYPE
}

lufthansa = requests.post('https://api.lufthansa.com/v1/oauth/token', data=data)

token = 'Bearer ' + lufthansa.json()['access_token']

headers = {
    'Authorization': token,
    'Accept': 'application/json',
}

response = requests.get('https://api.lufthansa.com/v1/mds-references/airports/FRA', headers=headers)


print(response.json())

