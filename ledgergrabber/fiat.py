import requests
from datetime import datetime


def from_fixer_io(base='USD', symbols=None, as_of=None):
    get_params = {'base': base}

    if symbols:
        get_params["symbols"] = ','.join(symbols)

    as_of = as_of or datetime.now()

    req_results = requests.get("https://api.exchangeratesapi.io/latest",
                               params=get_params).json()

    quotes = [(k, base, v, as_of) for k, v in req_results["rates"].items()]

    return quotes
