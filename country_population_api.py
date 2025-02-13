#!/usr/bin/env python3
import requests 
from data_eu import *

def format_country_population(country, population):
    """"Format population number with dot separators for readibility."""
    formatted_population = f"{population:,}".replace(",",".")
    return f"{country} has a population of {formatted_population} residents."



def get_population(country):

    if country == "Ireland":
        return f"{country} has a population of 5.262.000  residents."
    

    # Define API endpoint
    url = f"https://restcountries.com/v3.1/name/{country}"

    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: Unable to fetch data for {country} (Status {response.status_code})"
    
    data = response.json()

    # Extract relevant population info
    country_population = data[0].get("population", "Unknown")
    # Extract capital city name
    #capital_city = data[0].get("capital", ["Unknown"])[0]
     
    # Information with capital city name 
    #return f"{country}: {country_population} people. Capital: {capital_city}"

    # Information without capital city name
    return f"{format_country_population(country, country_population)}"

print(get_population("Italy"))
