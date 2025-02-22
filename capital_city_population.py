#!/usr/bin/env python3

import requests 
from data_eu import *


def format_population(population):
    """"Format population number with dot separators for readibility."""
    formatted_population = f"{population:,}".replace(",",".")
    return f"{formatted_population} residents"


def get_capital_population(result, api_key):
    """Fetches the population data for an EU capital city, ensuring correct country match."""
     # Determine city name based on the input type
    city_name = result[0] if isinstance(result, tuple) and len(result) == 3 else result
    # Ensure the city exists in the dictionary
    if city_name not in capital_iso:
        return f"No population data available for {city_name}."
    
    country_code = capital_iso[city_name] # Get the correct country code

    # Define API endpoint with country filter
    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    # Custom data for Valletta (original API data unavailable)
    if city_name == "Valletta":
        return "5.157 residents"
    """
     params = {
            "namePrefix": city_name,
            "countryIds": country_code,
            "limit": 1
    """
    # Custom data for Rome (original API data is incorect)
    if city_name == "Rome":
        return "2.760.000 residents"
    
    else:
        params = {
            "namePrefix": city_name, 
            "countryIds": country_code, # Ensures data is retrieved only from this country
            "limit": 1, # Get only the best match
            "minPopulation": 400000 # Exclude small cities with similar names
        }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }

    # Make API request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return f"Error: Unable to fetch data for {city_name} (Status {response.status_code})"

    # Parse JSON response
    data = response.json()
    cities = data.get("data",[])

    if not cities:
        return f"No population data found for {city_name}."
    
    population = cities[0].get("population", "Unknown")

    return format_population(population)


