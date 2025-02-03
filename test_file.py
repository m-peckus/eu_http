#!/usr/bin/env python3
from data_eu import *

def check_eu_capital(city, capitals, currencies):
    
    if city in eu_capitals:
        country = capitals[city]
        currency = currencies[city]
        #print(f"{city} is a capital city of {country}. Local currency is {currency}.")
        return city, country, currency
    else:
        #print(f"{city} is not in the list of EU capitals.")
        return city

# Example usage
#check_eu_capital("Stockholm", eu_capitals, eu_capital_currencies)   # Output: {input_city} is a capital city of {dictionary_value}



#print(country_data[0], country_data[2])
#check_eu_capital("London", eu_capitals)  # Output: {input_city} is not in the list of EU capitals.

