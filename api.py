""" All things API """

import requests
import json

APIKEY = "H56D8PS4NZ92U0R5"

def getTimeSeries(fx_pair: str, time_frame: str = "daily", output: str = "compact") -> dict[str,dict]:
  '''
  Fetches a time series  of the given currency pair from the API

  Parameters:
    fx_pair (str): Currency pair to fetch data for.
    time_frame (str): Timeframe of data (defaults to daily)
    output (str): Output format (defaults to compact)
  
  Returns:
    Dict: A dictionary with days as keys and ohlc data as values
  '''
  # Build URL
  base_url = "https://www.alphavantage.co/query?"
  # Linking function params to the  url parameters
  tf = time_frame.upper()
  from_currency = fx_pair.upper()[:3]
  to_currency = fx_pair.upper()[-3:]
  api_params = f"function=FX_{tf}&from_symbol={from_currency}&to_symbol={to_currency}&outputsize={output}&apikey=" + APIKEY
  
  # Requesting data from api
  r = requests.get(base_url + api_params)

  # delievering json data for requested time frame
  return r.json()[f"Time Series FX ({tf[0]+tf[1:].lower()})"]

# Used as confirmation that function is working correctly
print(json.dumps(getTimeSeries("EURUSD"), indent=2))