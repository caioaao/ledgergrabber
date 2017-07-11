import requests
from datetime import datetime


def from_coinmarketcap(base='USD', as_of=None):
    req_url = "https://api.coinmarketcap.com/v1/ticker/"
    quote_field = "price_" + base.lower()

    as_of = as_of or datetime.now()
    req_results = requests.get(req_url, params={'convert': base}).json()

    quotes = [(x["symbol"], base, x[quote_field], as_of)
              for x in req_results]

    return quotes
