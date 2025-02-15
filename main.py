#!/usr/bin/env python3

from user_input import *
from weather_api import city_temperature
from currency_api import currency_rate
from country_population_api import get_population
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access API key from .env file
API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    user_input = input(
        "Enter the name of an EU capital city to get:\n"
        "- Confirmation of EU capital status\n"
        "- Country population data\n"
        "- Local currency & exchange rate (if not Euro)\n"
        "- Local temperature\n"
        "- Enter any other city name to check if it's an EU capital.\n- Or press 5 to exit\n"
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
        country_population = get_population(result)

    if temperature is None:
        print("Unable to retrieve temperature data. Please try again later.")

    if isinstance(result, tuple) and len(result) == 3:
        city, country, currency = result
        if currency != "Euro":
            print(
                f"{city} is a capital city of {country}.\n"
                f"- Population of {country} is {country_population}.\n"
                f"- Local currency is {currency}.\n"
                f"- 1 {currency} equals to {rate} Euro.\n"
                f"- Weather temperature in {city} is {temperature}°C\n"
                )
        if currency == "Euro":
            print(
                f"{city} is a capital city of {country}.\n"
                f"- Population of {country} is: {country_population}.\n"
                f"- Local currency is {currency}.\n"
                f"- Weather temperature in {city} is {temperature}°C\n"
                )
        
    else:
        print(
            f"{result} is not in the list of EU capitals.\n"
            f"- Weather temperature in {result} is {temperature} °C\n"
            )

