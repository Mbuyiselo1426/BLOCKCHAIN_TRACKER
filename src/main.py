from src.tracker import track_wallet
import os
from src.blockchain_api import fetch_latest_transactions
from src.sheet_manager import get_sheet_client

if __name__ == "__main__":
    print("Starting blockchain tracker...")
    track_wallet()

#added a fumction
def run_tracker():
    wallet = os.getenv("WALLET_ADDRESS")
    sheet_id = os.getenv("SPREADSHEET_ID")
    
    print(f"🔎 Scanning Blockchain for wallet: {wallet[:10]}...")
    
    # 1. Fetch real data
    new_data = fetch_latest_transactions(wallet)
    
    if not new_data:
        print("No new transactions found.")
        return

    # 2. Connect to Sheets
    client = get_sheet_client()
    sheet = client.open_by_key(sheet_id).get_worksheet(0)
    
    # 3. Push to Sheets
    print("📝 Writing to Google Sheets...")
    for row in new_data:
        sheet.append_row(row)
        
    print("✅ Done! Your sheet is updated with real blockchain data.")

if __name__ == "__main__":
    run_tracker()
#this are the running commands
#python -m src.main
