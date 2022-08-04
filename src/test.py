#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 12:26:53 2022

@author: houda.el-mir
"""
import dst_utils as lu
import dst_extract as de




###########################################################Lufthansa####################################################

# Authentification
auth = lu.Authentication(client_key = "exzk4xtp9pr3txzssb2zqqd4", client_secret = "PfMrRRe6AyyB4kTJWdSx")

# get header
header = auth.get_header()
#print(header)
# Instanciation de la classe RequestFactory du module dst_utils
rf = lu.RequestFactory(header)

## donnees statiques 
# Instanciation de la classe DstStatic du module dst_extract
dd = de.LufthansaStatic(rf)

# affichage des donnees des aerports
print(dd.get_airport_data_luf("ALL"))

# Sauvegarder dans un fichier json
dd.get_airport_data_luf("ALL", write_json = True)
# affichage des donnees des pays
print(dd.get_countries_data_luf("ALL"))

## Donnees variables 
# Instanciation de la classe DstVariable du module dst_extract
ddv = de.LufthansaVariable(rf)

#affichage des donnees du vol en provenance de New York et a destination de France en date du 27/07/2022
ddv.pprint(ddv.get_flight_route("JFK", "FRA",  "2022-08-01"))

#Sauvegarder dans un fichier json 
ddv.get_flight_route("JFK", "FRA",  "2022-08-01", write_json = True)

#affichage des vols (plusieurs vols a la fois pour une periode) du 01 au 29 juillet 2022 
ddv.pprint(ddv.get_flights(write_json=True,startDate="01JUL22",endDate="29JUL22",daysOfOperation="1234567", timeMode = "UTC", flightType="passenger"))


###########################################################Airlabs####################################################
## Donnees temps reel 

api_key = "12de9152-83be-44ae-a711-958190764930"

# Instanciation de la classe DstRealTime du module dst_extract
drt = de.DstRealTime(api_key)

# affichage des donnees de tous les vols en temps reel
drt.get_flights(write_json=True)

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
# instanciation de la classe AirlabsVariable du module dst_extract

dav = de.AirlabsVariable(api_key)

dav.get_fleets_airlabs('LH')
