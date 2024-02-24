""" All things API """

import requests
import json

fx_pair = "EURUSD"

url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey==H56D8PS4NZ92U0R5'

apikey = "H56D8PS4NZ92U0R5"
r = requests.get(url)
data = r.json()

#print(json.dumps(data, indent=2))

print(data)
print(r)