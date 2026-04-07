from src.sheet_manager import connect_sheet
import os

def track_wallet():
    client = connect_sheet()
    
    if client is None:
        return None

    # Use the ID we extracted earlier
    sheet_id = "1moUTNlg9C84H7kpIU1_hXibgG5sOlB2l1NsImKsswtY"
    
    try:
        # Client opens the spreadsheet
        spreadsheet = client.open_by_key(sheet_id)
        # Spreadsheet gets the specific worksheet
        sheet = spreadsheet.get_worksheet(0)
        return sheet
    except Exception as e:
        print(f"❌ Error in tracker.py: {e}")
        return None