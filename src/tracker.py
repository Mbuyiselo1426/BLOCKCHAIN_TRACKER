from src.sheet_manager import connect_sheet # This matches your grep!
import os

def track_wallet():
    # This function connects to the sheet and sets it up
    client = connect_sheet()
    sheet_id = os.getenv("SPREADSHEET_ID")
    sheet = client.open_by_key(sheet_id).get_worksheet(0)
    return sheet
