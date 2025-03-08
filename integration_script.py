#!/usr/bin/env python3

import asyncio
import aiohttp
import math
import os
from dotenv import load_dotenv
from nested_eu_data import *
from data_fetcher import get_data

city = "Bucharest"
country = "Romania"
data = get_data(city, country)

#print(f"{city} Temperature: {data['temperature']}")
#print(f"Exchange Rate: {data['exchange_rate']}")
#print(f"City Population: {data['city_population']}")
#print(f"Country Population: {data['country_population']}")
