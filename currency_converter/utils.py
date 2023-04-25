import requests

# Replace "YOUR_API_KEY" with your actual API key from Apilayer
API_KEY = "iXoFQv4XxNB5LRwWD3PO8SH55Te5ehQc"

# API endpoint URL for converting currencies
API_URL = "https://api.apilayer.com/exchangerates_data/convert"

def convert_currency(amount, currency_from, currency_to, api_key):
    if not amount:
        return 0.0
    amount = float(amount)
    url = f"https://api.apilayer.com/exchangerates_data/convert"
    params = {"apikey": api_key, "from": currency_from, "to": currency_to, "amount": amount}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        converted_amount = data["result"]
        return converted_amount
    else:
        return None
