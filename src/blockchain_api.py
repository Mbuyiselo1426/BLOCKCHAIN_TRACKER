import requests
from src.config import ETHERSCAN_API_KEY, WALLET_ADDRESS
import os
import requests
from dotenv import load_dotenv



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
load_dotenv()

def fetch_latest_transactions(wallet_address):
    api_key = os.getenv("ETHERSCAN_API_KEY")
    # API URL to get the last 5 normal transactions
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&page=1&offset=5&sort=desc&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "1":
            transactions = data["result"]
            rows_for_sheet = []
            for tx in transactions:
                # Convert Wei (the smallest unit) to ETH
                eth_value = float(tx["value"]) / 10**18 
                
                # Matching your sheet columns: [TxHash, From, To, Value]
                rows_for_sheet.append([
                    tx["hash"], 
                    tx["from"], 
                    tx["to"], 
                    eth_value
                ])
            return rows_for_sheet
        else:
            print(f"Etherscan says: {data['message']}")
            return []
    except Exception as e:
        print(f"Error connecting to Etherscan: {e}")
        return []
