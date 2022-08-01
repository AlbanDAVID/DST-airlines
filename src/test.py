#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: houda.el-mir
"""
import lufthansa_utils as lu
import dst_extract as de 
import json
auth = lu.Authentication(client_key = "exzk4xtp9pr3txzssb2zqqd4", client_secret = "PfMrRRe6AyyB4kTJWdSx")
header = auth.get_header()

rf = lu.RequestFactory(header)

dd = de.DstStatic(rf)

print(dd.get_airport_data("ALL"))

ddv = de.DstVariable(rf)

#print(ddv.get_flight_route("JFK", "FRA",  "2022-07-27"))

print(json.dumps(ddv.get_flight_route("JFK", "FRA",  "2022-07-27"), indent=4, sort_keys=True))

aeroports_data = json.dumps(dd.get_airport_data("ALL"), indent=4, sort_keys=True)
aircrafts_data = json.dumps(dd.get_aircraft_data("ALL"), indent=4, sort_keys=True)
airlines_data = json.dumps(dd.get_airline_data("ALL"), indent=4, sort_keys=True)
countries_data = json.dumps(dd.get_countries_data("ALL"), indent=4, sort_keys=True)
cities_data = json.dumps(dd.get_cities_data("ALL"), indent=4, sort_keys=True)

ddv.pprint(ddv.get_flights(flightType="passenger", startDate="01JUL22",endDate="29JUL22",daysOfOperation="1234567", timeMode = "UTC"))

















