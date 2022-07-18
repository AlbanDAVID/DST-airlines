import requests
import json

params = {
  'api_key': 'fdab6336-d852-468d-8045-fb8350748f74',
  'flight_iata': 'LH1706'
}
method = 'flight'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))
