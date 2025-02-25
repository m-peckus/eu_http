#!/usr/bin/env python3

import requests
from data_eu import eu_currencies

def currency_rate(result):
    city = result[0] if isinstance(result, tuple) and len(result) == 3 else result
    # Returns the value of the item with the specified key
    currency = eu_currencies.get(city)

    if currency != "EUR":
        foreign_currency = currency  # New variable for non-Euro currencies
        """
        print(f"Local currency in {city} is {foreign_currency}.")
        print(f"Exchange rate API call will use: {foreign_currency}")
        """
        # API call using `foreign_currency` variable
        url = f"https://api.frankfurter.app/latest?from=EUR&to={foreign_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            foreign_currency_rate = data['rates'][f'{foreign_currency}']
            foreign_currency_to_eur = round(1 / foreign_currency_rate, 4)
            return foreign_currency_to_eur
    #else:
       # info = f"Local currency in {city} is Euro (no exchange rate needed)."
       # return info
        """
        print(f"Local currency in {city} is Euro (no exchange rate needed).")
        """

# Test examples
"""
get_currency_info("Copenhagen")
get_currency_info("Berlin")
get_currency_info("Warsaw")

"""
# rate = get_currency_info(city)
#print(f"Exchange rate to EUR: {rate}")