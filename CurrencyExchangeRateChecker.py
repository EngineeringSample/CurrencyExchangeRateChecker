import requests
import time

# Initialize API keys and URL list
api_keys = []
api_urls = []

# Get API keys
while True:
    api_key = input("Enter an API key (type 'q' to finish setup): ")
    if api_key == 'q':
        break
    api_keys.append(api_key)

# Get the API URL, use the default URL if the user doesn't provide one
api_url = input("Enter the API URL (default is https://open.er-api.com/v6/latest/): ").strip() or "https://open.er-api.com/v6/latest/"

# Get the base and target currencies
base_currency = input("Enter the base currency code (e.g., USD, EUR, GBP): ").upper()
target_currency = input("Enter the target currency code (e.g., USD, EUR, GBP): ").upper()

def get_exchange_rate(api_key, api_url):
    url = f"{api_url}{base_currency}"
    response = requests.get(url, params={"apikey": api_key})

    if response.status_code == 200:
        data = response.json()
        rates = data.get("rates", {})
        if target_currency in rates:
            exchange_rate = rates[target_currency]
            return exchange_rate
    return None

def fetch_exchange_rate():
    for api_key in api_keys:
        exchange_rate = get_exchange_rate(api_key, api_url)
        if exchange_rate is not None:
            return exchange_rate

    return None

def main():
    while True:
        exchange_rate = fetch_exchange_rate()
        if exchange_rate is not None:
            print(f"1 {base_currency} to {target_currency} exchange rate: {exchange_rate}")
        else:
            print("Unable to fetch exchange rate data")

        # Sleep for 30 minutes
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()
