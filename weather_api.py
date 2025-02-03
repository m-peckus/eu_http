#!/usr/bin/env python3

# Import modules
import requests
import math
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Access API key from .env file
API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')

def city_temperature(result, api_key):
    # Determine the city name based on the input type
    city = result[0] if isinstance(result, tuple) and len(result) == 3 else result

    # API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors

        data = response.json()

        # Check if temperature data exists
        if 'main' in data and 'temp' in data['main']:
            temp_kelvin = data['main']['temp']
            temp_celsius = math.floor(temp_kelvin - 273.15)
            return temp_celsius
        else:
            print(f"Temperature data not found for {city}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: Client side error")
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred: {req_err}")
    except (KeyError, TypeError, ValueError) as data_err:
        print(f"Data processing error: {data_err}")

    return None

