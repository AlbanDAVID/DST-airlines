import requests
import json
from static import * 




params = {
  'api_key': API_KEY,
  'flight_iata': 'LH1706'
}
method = 'flight'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

print(json.dumps(api_response, indent=4, sort_keys=True))
