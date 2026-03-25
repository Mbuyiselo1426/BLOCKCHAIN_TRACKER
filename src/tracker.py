# src/tracker.py
from src.sheet_manager import connect_sheet

def track_wallet():
    try:
        sheet_creds = connect_sheet()
        print("✅ Successfully connected to Google Sheets!")
        # TODO: Add your wallet tracking logic here
    except Exception as e:
        print(f"❌ Error connecting to Google Sheets: {e}")