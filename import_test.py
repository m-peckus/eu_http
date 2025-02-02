#!/usr/bin/env python3
from test_file import *
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    user_input = input(
        "Enter the name of an EU capital city to get:\n"
        "- Local temperature\n"
        "- Local currency & exchange rate (if not Euro)\n"
        "- 5 latest country-related news headlines\n"
        "- Confirmation of EU capital status\n"
        "\nEnter any other city name to check if it's an EU capital.\n"
        "Press 5 to exit: "
    )

    if user_input == '5':
        print("Exiting the program. Goodbye!")
        break
    
    clear_screen()

    # Edge Case 1: Check if the input is an integer
    if user_input.isdigit():
        print("Invalid input: Please enter a valid city name, not a number\n")
        continue

    # CONTINUE FROM HERE !

    result = check_eu_capital(user_input, eu_capitals, eu_capital_currencies)

    if isinstance(result, tuple) and len(result) == 3:
        city, country, currency = result
        print(f"\n{city} is a capital city of {country}. Local currency is {currency}.\n")
        # Future API calls will be integrated here
    else:
        print(f"{result} is not in the list of EU capitals.")

