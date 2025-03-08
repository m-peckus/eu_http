#!/usr/bin/env python3

import wikipediaapi
from nested_eu_data import *
USER_AGENT = "Wikipedia-API/1.0 (https://github.com/m-peckus/eu_http; martinpeckus@gmail.com)"

def get_wikipedia_population(city):
    """Fetch city population from Wikipedia API."""

    if city not in eu_data:
        return f"{city} no such city in eu_data."
    
    # Initialize Wikipedia API with custom user-agent
    wiki = wikipediaapi.Wikipedia("en")
    wiki.session.headers.update({"User-Agent": USER_AGENT})

    # Fetch Wikipedia page for the city
    page = wiki.page(city)
    if not page.exists():
        return f"Wikipedia page for {city} not found."
    
    # Extract summary text
    summary_text = page.summary

    # Look for population related data
    for sentence in summary_text.split("."):
        if "population" in sentence.lower() or "residents" in sentence.lower():
            return f"Population of {city}: {sentence.strip()}."
    
    return f"Population data for {city} not found in Wikipedia API."


# Example usage
city_name = "Paris"
print(get_wikipedia_population(city_name))

