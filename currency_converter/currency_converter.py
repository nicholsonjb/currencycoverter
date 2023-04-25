"""
Currency Converter Utility
Author: James Nicholson
Date: 04/24/2023
Description: This utility provides a function for converting currencies using real-time exchange rates from the Apilayer API.
"""


import requests

# Replace "YOUR_API_KEY" with your actual API key from Apilayer
api_key = "iXoFQv4XxNB5LRwWD3PO8SH55Te5ehQc"

# API endpoint URL for getting exchange rates
url = f"https://api.apilayer.com/exchangerates_data/{api_key}"

# Define function to convert currency
def convert_currency(amount, currency_from, currency_to):
    params = {"access_key": api_key}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        from_rate = rates[currency_from]
        to_rate = rates[currency_to]
        exchange_rate = to_rate / from_rate
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)
    else:
        return None
