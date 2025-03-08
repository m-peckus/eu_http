#!/usr/bin/env python3

import requests 
from nested_eu_data import *
# from data_eu import *

def format_country_population(population):
    """"Format population number with dot separators for readibility."""
    return f"{population:,}".replace(",",".") + "residents"


def get_population(result):
    """Fetches the population data for a country, ensuring correct data retrieval."""

    # Determine country name based on input type
    country = result[1] if isinstance(result, tuple) and len(result) == 3 else result

    # Custom population data for Ireland (API data is incorrect)
    if country == "Ireland":
        return format_country_population(5262000)
    
    # Define API endpoint
    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: Unable to fetch data for {country} (Status {response.status_code})"
    
    data = response.json()

    # Ensure valid data response
    if not data or not isinstance(data, list) or "population" not in data[0]:
        return f"No population data found for {country}."
    
    # Extract and format population data
    country_population = data[0]["population"]
    return format_country_population(country_population)

