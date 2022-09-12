#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: houda.el-mir
"""

import dst_utils as lu
import LufthansaStatic 
import LufthansaVariable 
import AirlabsStatic
import AirlabsVariable
import DstRealtime
import requests
import static



###########################################################Lufthansa####################################################

# Authentification
auth = lu.Authentication(client_key = static.client_id_luf, client_secret = static.client_secret_luf)

# get header
header = auth.get_header()
#print(header)
# Instanciation de la classe RequestFactory du module dst_utils
rf = lu.RequestFactory(header)



## donnees statiques 
# Instanciation de la classe DstStatic du module dst_extract
dd = LufthansaStatic.LufthansaStatic(rf)

# affichage des donnees des aerports
print(dd.get_airport_data_luf())

# Sauvegarder dans un fichier json
dd.get_airport_data_luf(write_json = True)
# affichage des donnees des pays
json_text = dd.get_countries_data_luf()

dd.get_cities_data_luf(write_json=True)

## Donnees variables 
# Instanciation de la classe DstVariable du module dst_extract
ddv = LufthansaVariable.LufthansaVariable(rf)

#affichage des donnees du vol en provenance de New York et a destination de France en date du 27/07/2022
ddv.pprint(ddv.get_flight_route("JFK", "FRA",  "2022-08-29"))

#Sauvegarder dans un fichier json 
ddv.get_flight_route("JFK", "FRA",  "2022-08-01", write_json = True)

#affichage des vols (plusieurs vols a la fois pour une periode) du 01 au 29 juillet 2022 
ddv.pprint(ddv.get_flights(write_json=True,startDate="01JUL22",endDate="29JUL22",daysOfOperation="1234567", timeMode = "UTC", flightType="passenger"))


###########################################################Airlabs####################################################
## Donnees temps reel 

api_key = static.api_key_airlabs3

# Instanciation de la classe DstRealTime du module dst_extract
drt = DstRealtime.DstRealTime(api_key)

# affichage des donnees de tous les vols en temps reel
print(drt.get_flights(write_json=False))

# affichage des delays de tous les vols concernés par un retard
drt.get_delays('40', 'departures', 'LH', False)

# Affichage des donnees de tous les vols Lufthansa en temps reel
drt.get_flights_by_airline_iata('LH')

#Donnees temps reel du vol (un seul) 'LH2001' 
drt.get_flight_by_flight_iata('LH2001')

drt.get_delays_by_airline_iata('LH')

# instanciation de la classe AirlabsStatic du module dst_extract
das = de.AirlabsStatic(api_key)
das.get_airlines_airlabs(write_json=True)
das.get_cities_airlabs()
das.get_airports_airlabs()
# instanciation de la classe AirlabsVariable du module dst_extract

dav = de.AirlabsVariable(api_key)

dav.get_fleets_airlabs('LH')

requests.get("https://airlabs.co/api/v9/airports?iata_code=CDG&api_key={api_key}".format(api_key = api_key)).json()

dd.get_nearest_airports_luf( 7.62, 44.54)
dd.get_nearest_airports_luf( 48.50, 2.20)
dd.get_nearest_airports_luf( -65.3, -24.19)
#get info 

print(das.get_airports_airlabs(write_json=True))







