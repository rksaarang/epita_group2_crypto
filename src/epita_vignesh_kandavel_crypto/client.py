import requests

from .config import config

BASE_URL = "https://min-api.cryptocompare.com/data/pricemultifull"


def fetch_live_data() -> dict:
    """Fetch live Bitcoin and Ethereum prices from CryptoCompare."""
    config.validate()

    params = {
        "fsyms": "BTC,ETH",
        "tsyms": "USD,EUR",
    }

    headers = {
        "authorization": f"Apikey {config.api_key}"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()
    payload = response.json()

    raw = payload.get("RAW", {})
    result = {"status": "LIVE_SUCCESS"}

    for symbol in ("BTC", "ETH"):
        if symbol not in raw:
            continue

        for currency in ("USD", "EUR"):
            details = raw[symbol].get(currency, {})

            if details:
                result[f"{symbol}_{currency}_price"] = details.get("PRICE")
                result[f"{symbol}_{currency}_market_cap"] = details.get("MKTCAP")

    if len(result) == 1:
        raise ValueError("No cryptocurrency price data returned by CryptoCompare.")

    return result