#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: houda.el-mir
"""
import lufthansa_utils as lu
import dst_extract as de 

auth = lu.Authentication(client_key = "exzk4xtp9pr3txzssb2zqqd4", client_secret = "PfMrRRe6AyyB4kTJWdSx")
rf = lu.RequestFactory(auth.get_header())

dd = de.DstStatic(rf)

print(dd.get_airport_data("ALL"))


ddv = de.DstVariable(rf)

#print(ddv.get_flight_route("JFK", "FRA",  "2022-07-27"))
import json
print(json.dumps(ddv.get_flight_route("JFK", "FRA",  "2022-07-27"), indent=4, sort_keys=True))

aeroports_data = json.dumps(dd.get_airport_data("ALL"), indent=4, sort_keys=True)
aircrafts_data = json.dumps(dd.get_aircraft_data("ALL"), indent=4, sort_keys=True)
airlines_data = json.dumps(dd.get_airline_data("ALL"), indent=4, sort_keys=True)
countries_data = json.dumps(dd.get_countries_data("ALL"), indent=4, sort_keys=True)
cities_data = json.dumps(dd. get_cities_data("ALL"), indent=4, sort_keys=True)


print(json.dumps(ddv.get_flight_by_flight_number('LH1290', '2022-07-21'), indent=4, sort_keys=True))
