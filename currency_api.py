#!/usr/bin/env python3

import requests
from data_eu import eu_currencies

def currency_rate(result):
    """Fetches exchange rate if the local currency is not Euro"""
    city = result[0] if isinstance(result, tuple) and len(result) == 3 else result
    currency = eu_currencies.get(city)

    if currency == "EUR":
        return f"Local currency in {city} is Euro (no exchange rate needed)."
        
    # API call using `foreign_currency` variable
    url = f"https://api.frankfurter.app/latest?from=EUR&to={currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        exchange_rate = data.get("rates",{}).get(currency)

        if exchange_rate:
            return round(1 / exchange_rate, 2)
        else:
            return f"Error: Exchange rate for {currency} not found."
    
    return f"Error: Unable to fetch exchange rate (Status {response.status_code})."
    

        