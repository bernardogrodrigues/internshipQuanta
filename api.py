""" All things API """

import requests
import json

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# H56D8PS4NZ92U0R5
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NASDX&interval=1min&apikey=H56D8PS4NZ92U0R5'
r = requests.get(url)
data = r.json()

print(json.dumps(data, indent=2))