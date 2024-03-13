import requests
from datetime import datetime
import json

APIKEY = "7QE001W0RV3REU6S"

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

  # [{'date': datetime, 'open': float, 'high': float, 'low': float, 'close': float}, ...]
  data: list[dict] = []

  for date, values in r.json()[f"Time Series FX ({tf[0]+tf[1:].lower()})"].items():
    data.append({
        # Convert date from string to datetime object for easier handling in plots
        'date': datetime.strptime(date, '%Y-%m-%d'),
        'open': float(values['1. open']),
        'high': float(values['2. high']),
        'low': float(values['3. low']),
        'close': float(values['4. close'])#,
        #'volume': float(values['5. volume'])
    })

  # delievering ohlc data for requested time frame as a list of dicts
  return data

# Used as confirmation that function is working correctly
#print(getTimeSeries("EURUSD"))