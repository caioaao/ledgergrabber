import requests
from datetime import datetime


def from_coinmarketcap(base='USD', limit=200, as_of=None, api_key=None):
    if not api_key:
        req_url = "https://api.coinmarketcap.com/v1/ticker/"
        headers = {}
    else:
        req_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        headers = {'X-CMC_PRO_API_KEY': api_key}

    req_params = {'convert': base, 'limit': limit}

    as_of = as_of or datetime.now()
    req_results = requests.get(req_url, params=req_params, headers=headers).json()


    quotes = [(x["symbol"], base, x['quote'][base]['price'], as_of)
              for x in req_results['data']
              if x['quote'][base] and x['symbol'] != base]

    return quotes


def btc_from_foxbit(base='USD', as_of=None):
    req_url = "https://api.blinktrade.com/api/v1/" + base + "/ticker"

    as_of = as_of or datetime.now()

    req_results = requests.get(req_url).json()

    val = (req_results['buy'] + req_results['sell']) / 2

    return ('BTC', base, val, as_of)
