import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

wallet = os.getenv("WALLET_ADDRESS")
api_key = os.getenv("ETHERSCAN_API_KEY")

url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": 1,
    "module": "account",
    "action": "txlist",
    "address": wallet,
    "startblock": 0,
    "endblock": 99999999,
    "page": 1,
    "offset": 5,
    "sort": "desc",
    "apikey": api_key
}

response = requests.get(url, params=params, timeout=30)
data = response.json()

print("HTTP status:", response.status_code)
print("Etherscan message:", data.get("message"))
print("Result status:", data.get("status"))

if data.get("status") == "1":
    transactions = data.get("result", [])
    print("Transactions retrieved:", len(transactions))

    for tx in transactions:
        print("Hash:", tx["hash"])
        print("From:", tx["from"])
        print("To:", tx["to"])
        print("Value (ETH):", int(tx["value"]) / 10**18)
else:
    print("Etherscan error:", data.get("result"))
