import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE")
SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")