from src.sheet_manager import connect_sheet
from src.config import SPREADSHEET_ID, WORKSHEET_NAME


def track_wallet():
    client = connect_sheet()

    if client is None:
        return None

    if not SPREADSHEET_ID:
        print("❌ SPREADSHEET_ID is missing from .env")
        return None

    try:
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        sheet = spreadsheet.worksheet(WORKSHEET_NAME)

        print(f"✅ Connected to Google Sheet: {spreadsheet.title}")
        print(f"✅ Using worksheet: {sheet.title}")

        return sheet

    except Exception as e:
        print(f"❌ Error in tracker.py: {e}")
        return None
