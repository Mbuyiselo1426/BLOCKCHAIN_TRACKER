# #this are the running commands
# #python -m src.main
import os
from src.tracker import track_wallet
from src.blockchain_api import fetch_latest_transactions

def run_tracker():
    print("🚀 Starting the Blockchain Tracker...")
    
    # 1. Get the wallet address from .env
    wallet = os.getenv("WALLET_ADDRESS")
    
    # 2. Fetch the data using the function from blockchain_api.py
    print(f"🔎 Fetching data for {wallet[:10]}...")
    new_rows = fetch_latest_transactions(wallet)
    
    if not new_rows:
        print("❌ No transactions found or API error.")
        return

    # 3. Get the Google Sheet object from tracker.py
    sheet = track_wallet()
    
    if sheet is None:
        print("🛑 Critical Error: Could not connect to the Google Sheet. Check your permissions!")
        return # Stop the script before it crashes
    # 4. Write the data
    print("📝 Writing to Google Sheets...")
    for row in new_rows:
        sheet.append_row(row)
    
    print("✅ Sync Complete!")

if __name__ == "__main__":
    run_tracker()