import pytest
import dst_utils as du
import DstRealtime as dr
import LufthansaStatic as ls
import LufthansaVariable as lv
import AirlabsStatic as als
import AirlabsVariable as alv
import json
import static

## Auth
auth = du.Authentication(client_key=static.client_id_luf, client_secret= static.client_secret_luf)
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
    api_key = static.api_key_airlabs2

    # Instanciation de la classe DstRealTime du module dst_extract
    drt = dr.DstRealTime(api_key)

    # affichage des donnees de tous les vols en temps reel
    assert drt.get_flights(write_json=False)['request']['currency'] == 'USD'
