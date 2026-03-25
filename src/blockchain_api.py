import requests
from src.config import ETHERSCAN_API_KEY, WALLET_ADDRESS

BASE_URL = "https://api.etherscan.io/api"


def get_transactions():
    params = {
        "module": "account",
        "action": "txlist",
        "address": WALLET_ADDRESS,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()