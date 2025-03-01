#!/usr/bin/env python3

import requests 
import json
import os
from datetime import datetime, timedelta
from nested_eu_data import *

# Hardcoded population data for cities with incorrect/missing API values
fixed_populations = {
    "Valletta": "5.157 residents",
    "Rome": "2.760.000 residents"
}


CACHE_FILE = "city_population_cache.json"
CACHE_EXPIRATION_DAYS = 40

def load_cache():
    """Load cached city population data from file. Handling empty or missing files safely."""
    #if os.path.exists(CACHE_FILE):
        #with open(CACHE_FILE, "r") as file:
            #return json.load(file)
    #return {}
    if not os.path.exists(CACHE_FILE):
        return {} # Return empty dictionary if file doesn't exist

    try:
        with open(CACHE_FILE, "r")as file:
            return json.load(file) # Load JSON data
    except json.JSONDecodeError:
        return {} # Return empty dict if file is empty or invalid


def save_cache(cache):
    """Save updated city population data to file."""
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file, indent=4)

def format_population(population):
    """"Format population number with dot separators for readibility."""
    return f"{population:,}".replace(",",".") + " residents"

def get_capital_population(result, api_key):
    """Fetches the population data for an EU capital city, ensuring correct country match."""

     # Extract city name from input
    city_name = result[0] if isinstance(result, tuple) and len(result) == 3 else result

    # Return hardcoded data if city is in fixed_populations
    if city_name in fixed_populations:
        return fixed_populations[city_name]

    # Load cache
    cache = load_cache()
    
    # Check if city exists in cache and is still valid
    if city_name in cache:
        last_updated = datetime.fromisoformat(cache[city_name]["last_updated"])
        if datetime.now() - last_updated < timedelta(days=CACHE_EXPIRATION_DAYS):
            return cache[city_name]["population"]

    
    # Check if city exists in nested dictionary
    if city_name not in eu_data:
        return f"No population data available for {city_name}."
    
    # Define API request parameters
    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    params = {
            "namePrefix": city_name, 
            "countryIds": eu_data[city_name]["iso_code"], # Ensures correct iso code country match
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


        population = format_population(cities[0].get("population", "Unknown"))

        # Update cache
        cache[city_name] = {
            "population": population,
            "last_updated": datetime.now().isoformat()
        }
        save_cache(cache)

        return population

    except requests.exceptions.RequestException as e:
        return f"Error fetching data for {city_name}: {e}"

