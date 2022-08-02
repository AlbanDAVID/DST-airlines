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

print(dd.get_airport_data("JFK"))


ddv = de.DstVariable(rf)

print(ddv.get_flight_route("JFK", "FRA",  "2022-07-27"))