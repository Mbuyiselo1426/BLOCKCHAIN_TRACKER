import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

load_dotenv()

def connect_sheet():
    # This function is the "Key Maker"
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive" # Added Drive scope for better access
    ]
    
    creds_file = os.getenv("CREDENTIALS_FILE")
    
    if not creds_file or not os.path.exists(creds_file):
        print(f"❌ Credentials file not found at: {creds_file}")
        return None

    creds = Credentials.from_service_account_file(creds_file, scopes=scopes)
    client = gspread.authorize(creds)
    
    # CRITICAL: This must return the 'client' object
    return client