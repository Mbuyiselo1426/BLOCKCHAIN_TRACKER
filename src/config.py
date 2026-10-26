import os
from dotenv import load_dotenv

load_dotenv()


def _parse_csv_list(raw_value):
    if not raw_value:
        return []
    return [item.strip() for item in str(raw_value).split(",") if item.strip()]


CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", "").strip()
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "").strip()
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME", "Transactions").strip() or "Transactions"
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY", "").strip()
ETHERSCAN_API_URL = os.getenv("ETHERSCAN_API_URL", "https://api.etherscan.io/v2/api").strip() or "https://api.etherscan.io/v2/api"
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "").strip()
WALLET_ADDRESSES = _parse_csv_list(os.getenv("WALLET_ADDRESSES", ""))

if not WALLET_ADDRESSES and WALLET_ADDRESS:
    WALLET_ADDRESSES = [WALLET_ADDRESS]

DEFAULT_TIMEOUT = 10
