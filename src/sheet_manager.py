import gspread
from google.oauth2.service_account import Credentials
from src.config import CREDENTIALS_FILE, SPREADSHEET_NAME

def connect_sheet():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=scope
    )

    client = gspread.authorize(creds)
    return client.open_by_key("1moUTNlg9C84H7kpIU1_hXibgG5sOlB2l1NsImKsswtY").sheet1