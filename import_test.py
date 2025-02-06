#!/usr/bin/env python3

from test_file import *
from weather_api import city_temperature
from currency_api import currency_rate
import os 
import requests
import json
import math
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access API key from .env file
API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    user_input = input(
        "\nEnter the name of an EU capital city to get:\n\n"
        "- Local temperature\n"
        "- Local currency & exchange rate (if not Euro)\n"
        "- 5 latest country-related news headlines\n"
        "- Confirmation of EU capital status\n"
        "\nEnter any other city name to check if it's an EU capital.\n- Or press 5 to exit\n"
        "Enter city name : "
    )

    if user_input == '5':
        print("Exiting the program. Goodbye!")
        break
    
    clear_screen()

    if user_input.isdigit():
        print("Invalid input: Please enter a valid city name, not a number\n")
    elif not user_input.isalpha():
        print("Invalid input: City names should only contain letters\n")
    elif len(user_input) > 12:
        print("Invalid input: City names can't exceed 12 characters.\n")
    else:
        user_input = user_input.title()
        result = check_eu_capital(user_input, eu_capitals, eu_capital_currencies)
        temperature = city_temperature(result, API_KEY)
        rate = currency_rate(result)

    if temperature is None:
        print("Unable to retrieve temperature data. Please try again later.")

    if isinstance(result, tuple) and len(result) == 3:
        city, country, currency = result
        if currency != "Euro":
            print(f"\n{city} is a capital city of {country}. Local currency is {currency}.\nCurrency exchange rate is {rate}\nLocal temperature is {temperature}°C")
        if currency == "Euro":
            print(f"\n{city} is a capital city of {country}. Local currency is {currency}.\nLocal temperature is {temperature}°C")
        # Future API calls will be integrated here
    else:
        print(f"{result} is not in the list of EU capitals.\nLocal temperature in {result} is {temperature} °C\n")

