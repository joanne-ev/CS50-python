import sys
import requests
import json

try:
   n = float(sys.argv[1])
except IndexError:
   sys.exit('Missing command-line argument')
except ValueError:
   sys.exit('Command-line argument is not a number')


# Get request using the API key formatted as json that uses python dictionaries
response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=290a3119a7158a7ee4d8f441b14574237518758b0004c85cf1c98280cd53906d')
response_json = response.json()

# Cleans json file with indents after each key
response_view = json.dumps(response_json, indent = 2)

# Retrieve the current price of bitcoin from the inner dictionary
response_data = response_json['data']
curr_price = float(response_data['priceUsd'])

# Print current price of n bitcoins
curr_n_price = round(curr_price * n, 4)
print(f'${curr_n_price:,}')
