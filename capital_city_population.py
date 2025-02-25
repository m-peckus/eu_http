#!/usr/bin/env python3

import requests 
from data_eu import *

# Hardcoded population data for cities with incorrect/missing API values
fixed_populations = {
    "Valletta": "5.157 residents",
    "Rome": "2.760.000 residents"
}


def format_population(population):
    """"Format population number with dot separators for readibility."""
    return f"{population:,}".replace(",",".") + "residents"

def get_capital_population(result, api_key):
    """Fetches the population data for an EU capital city, ensuring correct country match."""

     # Extract city name from input
    city_name = result[0] if isinstance(result, tuple) and len(result) == 3 else result

    # Check if city exists in capital_iso
    if city_name not in capital_iso:
        return f"No population data available for {city_name}."
    
    # Return hardcoded data if city is in fixed_populations
    if city_name in fixed_populations:
        return fixed_populations[city_name]
    

    # Define API request parameters
    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    params = {
            "namePrefix": city_name, 
            "countryIds": capital_iso[city_name], # Ensures correct country match
            "limit": 1, # Get only the best match
            "minPopulation": 400000 # Exclude small cities with similar names
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status() # Raise exception for HTTP errors
        data = response.json()
        cities = data.get("data",[])

        if not cities:
            return f"No population data found for {city_name}."


        population = cities[0].get("population", "Unknown")
        return format_population(population)

    except requests.exceptions.RequestException as e:
        return f"Error fetching data for {city_name}: {e}"


