
import requests

from .config import config

BASE_URL = "https://min-api.cryptocompare.com/data"


def get_prices():
    config.validate()

    url = f"{BASE_URL}/pricemultifull"

    params = {
        "fsyms": "BTC,ETH",
        "tsyms": "USD,EUR",
    }

    headers = {
        "authorization": f"Apikey {config.api_key}",
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=15,
    )

    response.raise_for_status()
    return response.json()
