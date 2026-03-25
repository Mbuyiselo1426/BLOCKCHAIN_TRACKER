from src.sheet_manager import connect_sheet


def track_wallet():
    print("Connecting to Google Sheets...")
    sheet = connect_sheet()

    print("Writing test data...")

    row = ["test_hash", "from_address", "to_address", "1000"]
    sheet.append_row(row)

    print("Done.")