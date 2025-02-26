#!/usr/bin/env python3

eu_data = {
    "Vienna": {"country": "Austria", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "at"},
    "Brussels": {"country": "Belgium", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "be"},
    "Sofia": {"country": "Bulgaria", "currency_name": "Bulgarian Lev", "currency_code": "BGN", "iso_code": "bg"},
    "Zagreb": {"country": "Croatia", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "hr"},
    "Nicosia": {"country": "Cyprus", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "cy"},
    "Prague": {"country": "Czech Republic", "currency_name": "Czech Koruna", "currency_code": "CZK", "iso_code": "cz"},
    "Copenhagen": {"country": "Denmark", "currency_name": "Danish Krone", "currency_code": "DKK", "iso_code": "dk"},
    "Tallinn": {"country": "Estonia", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "ee"},
    "Helsinki": {"country": "Finland", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "fi"},
    "Paris": {"country": "France", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "fr"},
    "Berlin": {"country": "Germany", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "de"},
    "Athens": {"country": "Greece", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "gr"},
    "Budapest": {"country": "Hungary", "currency_name": "Hungarian Forint", "currency_code": "HUF", "iso_code": "hu"},
    "Dublin": {"country": "Ireland", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "ie"},
    "Rome": {"country": "Italy", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "IT"},
    "Riga": {"country": "Latvia", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "lv"},
    "Vilnius": {"country": "Lithuania", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "lt"},
    "Luxembourg": {"country": "Luxembourg", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "lu"},
    "Valletta": {"country": "Malta", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "mt"},
    "Amsterdam": {"country": "Netherlands", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "nl"},
    "Warsaw": {"country": "Poland", "currency_name": "Polish Zloty", "currency_code": "PLN", "iso_code": "pl"},
    "Lisbon": {"country": "Portugal", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "pt"},
    "Bucharest": {"country": "Romania", "currency_name": "Romanian Leu", "currency_code": "RON", "iso_code": "ro"},
    "Bratislava": {"country": "Slovakia", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "sk"},
    "Ljubljana": {"country": "Slovenia", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "si"},
    "Madrid": {"country": "Spain", "currency_name": "Euro", "currency_code": "EUR", "iso_code": "es"},
    "Stockholm": {"country": "Sweden", "currency_name": "Swedish Krona", "currency_code": "SEK", "iso_code": "se"}
}

city_data = eu_data["Athens"]
country = city_data["country"]
currency_name = city_data["currency_name"]
currency_code = city_data["currency_code"]
iso_code = city_data["iso_code"]
#print(eu_data["Warsaw"]["currency_code"])