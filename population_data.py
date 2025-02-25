#!/usr/bin/env python3

# File is not used in this project


import requests 
from data_eu import *
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Access API key for GeoDB from .env file
api_key = os.getenv('x-rapidapi-key')




def format_population(city_name, population):
    """"Format population number with dot separators for readibility."""
    formatted_population = f"{population:,}".replace(",",".")
    return f"{city_name} has a population of {formatted_population} residents."


def get_capital_population(city_name, api_key):
    """Fetches the population data for an EU capital city, ensuring correct country match."""

    # Ensure the city exists in the dictionary
    if city_name not in capital_iso:
        return f"No population data available for {city_name}."
    
    country_code = capital_iso[city_name] # Get the correct country code

    # Define API endpoint with country filter
    url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

    # Custom filtering for Valletta
    if city_name == "Valletta":
        params = {
            "namePrefix": city_name,
            "countryIds": country_code,
            "limit": 1
        }

    if city_name == "Rome":
        return f"{city_name} has a population of 2.760.000 residents."
    
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

    return format_population(city_name, population)


print(get_capital_population("Stockholm", api_key)) # Continue testing 

"""

# Dictionary mapping EU capitals to ISO 3166 country codes

"""
capital_iso = {
    "Vienna": "at",
    "Brussels": "be",
    "Sofia": "bg",
    "Zagreb": "hr",
    "Nicosia": "cy",
    "Prague": "cz",
    "Copenhagen": "dk",
    "Tallinn": "ee",
    "Helsinki": "fi",
    "Paris": "fr",
    "Berlin": "de",
    "Athens": "gr",
    "Budapest": "hu",
    "Dublin": "ie",
    "Rome": "it",
    "Riga": "lv",
    "Vilnius": "lt",
    "Luxembourg": "lu",
    "Valletta": "mt",
    "Amsterdam": "nl",
    "Warsaw": "pl",
    "Lisbon": "pt",
    "Bucharest": "ro",
    "Bratislava": "sk",
    "Ljubljana": "si",
    "Madrid": "es",
    "Stockholm": "se"
}

