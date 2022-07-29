#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: houda.el-mir
"""
import lufthansa_utils as lu
import dst_extract as de 

auth = lu.Authentication(client_key = "exzk4xtp9pr3txzssb2zqqd4", client_secret = "PfMrRRe6AyyB4kTJWdSx")
header = auth.get_header()

rf = lu.RequestFactory(header)

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
cities_data = json.dumps(dd.get_cities_data("ALL"), indent=4, sort_keys=True)

#accept: application/json" -H "Authorization: Bearer tvgcx4x55tvgykvjqqft6247"
print(header)
#test_request = rf.create_request("https://api.lufthansa.com/v1/flight-schedules/
#flightschedules/passenger?airlines=LH&startDate=04MAY22&endDate=10JUN22&daysOfOperation=
#1234567&timeMode=UTC")
#ddv.pprint(test_request)
ddv.pprint(ddv.get_flights(startDate="01JUL22",endDate="29JUL22",daysOfOperation="1234567", timeMode = "UTC"))

















