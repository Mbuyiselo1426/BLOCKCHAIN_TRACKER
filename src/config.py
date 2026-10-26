import os
from dotenv import load_dotenv

load_dotenv()


def _parse_csv_list(raw_value):
    if not raw_value:
        return []
    return [item.strip() for item in raw_value.split(",") if item.strip()]


CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", "")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME", "Transactions")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "")
WALLET_ADDRESSES = _parse_csv_list(os.getenv("WALLET_ADDRESSES", ""))

if not WALLET_ADDRESSES and WALLET_ADDRESS:
    WALLET_ADDRESSES = [WALLET_ADDRESS]
