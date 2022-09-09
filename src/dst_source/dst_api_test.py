import pytest
import dst_utils as du
import DstRealtime as dr
import LufthansaStatic as ls
import LufthansaVariable as lv
import AirlabsStatic as als
import AirlabsVariable as alv
import json

## Auth
auth = du.Authentication(client_key="exzk4xtp9pr3txzssb2zqqd4", client_secret="PfMrRRe6AyyB4kTJWdSx")
def test_auth():
    header = auth.get_header()
    assert header.get('accept') == 'application/json'

## Dst static

def test_luf_static_data():
    rf = du.RequestFactory(auth.get_header())
    lsi=ls.LufthansaStatic(rf)
    assert lsi.get_nearest_airports_luf(40, 40, False)['NearestAirportResource']['Airports']['Airport'][0]['AirportCode'] == 'ERC'

## Dst Variable

def test_luf_variable_data():
    rf = du.RequestFactory(auth.get_header())
    lsv=lv.LufthansaVariable(rf)
    assert lsv.get_flight_route("JFK", "FRA",  "2022-09-08", False)['FlightStatusResource']['Flights']['Flight'][0]['Arrival']['AirportCode'] == 'FRA'

## DST Real Time
def test_dst_real_time():
    api_key = "12de9152-83be-44ae-a711-958190764930"

    # Instanciation de la classe DstRealTime du module dst_extract
    drt = dr.DstRealTime(api_key)

    # affichage des donnees de tous les vols en temps reel
    assert drt.get_flights(write_json=False)['request']['currency'] == 'EUR'
