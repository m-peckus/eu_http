#!/usr/bin/env python3
from data_eu import *

def check_eu_capital(city, capitals, currencies):
    
    if city in eu_capitals:
        country = capitals[city]
        currency = currencies[city]
        return city, country, currency
    else:
        return city

