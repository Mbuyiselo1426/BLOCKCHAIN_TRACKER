import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from src.config import CREDENTIALS_FILE, SPREADSHEET_NAME
load_dotenv()



def connect_sheet():
    """
    Connect to Google Sheets using service account credentials
    defined in the .env file as CREDENTIALS_FILE.
    """
    # Get the JSON credentials file path from environment
    cred_file = os.getenv("CREDENTIALS_FILE")
    
    if not cred_file:
        raise ValueError("CREDENTIALS_FILE is not set in your .env file!")
    
    # Check if the file actually exists
    if not os.path.isfile(cred_file):
        raise FileNotFoundError(
            f"The credentials file was not found at: {cred_file}"
        )
    
    # Create credentials object
    creds = Credentials.from_service_account_file(cred_file)
    
    return creds

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
    return client.open(SPREADSHEET_NAME).sheet1