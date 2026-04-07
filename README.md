What This Project Will Do

Your tracker will:

✔ connect to Etherscan API
✔ fetch wallet transactions
✔ store them in Google Sheets

1️⃣ Python starts with src/main.py
2️⃣ main.py calls the function in tracker.py
3️⃣ tracker.py should:

call blockchain_api.py

fetch blockchain transactions

connect to Google Sheets

write the transactions to the sheet


1. The High-Level Definition
"The Blockchain Tracker is an automation tool that bridges a traditional database (Google Sheets) with a Decentralized Ledger (Blockchain). It allows a user to record financial transactions in a spreadsheet and automatically 'notarize' them on a blockchain testnet for permanent, tamper-proof record-keeping."

2. The Problem it Solves
The Problem: Spreadsheets are easy to use1️⃣ Add real blockchain data (Etherscan)

Get your API key and plug it back in so your sheet shows real transactions, not test data., but anyone with access can delete or change the data. There is no "permanent" proof that a transaction happened at a specific time.

The Solution: By sending the data to a blockchain, you create a Transaction Hash. Even if someone deletes the row in Excel, the record lives forever on the blockchain (Sepolia or Amoy).

3. How it Works (The 3-Step Flow)
When you explain this to someone, describe it in these three phases:

The Input (Google Sheets API):

The user types an expense (e.g., "Bought Laptop - $500") into a Google Sheet.

Our Python script monitors the sheet using a Service Account (that’s what your credentials.json is for).

The Bridge (Web3.py):

The script picks up that new row.

It connects to a Blockchain Provider (like Alchemy or Infura).

It signs a transaction using a private key and sends the data to a Smart Contract or a simple wallet transfer on a testnet.

The Receipt (The Feedback Loop):

Once the blockchain confirms the transaction, it generates a Transaction Hash (a long string of letters and numbers).

The script writes that Hash back into the Google Sheet next to the expense. This is the "Digital Receipt."

4. Your Tech Stack (The "How")
If someone asks what you are using to build it, you say:

Language: Python 3 (Moving towards a TDD approach).

APIs: Google Sheets API & Google Drive API.

Blockchain: Web3.py library connecting to the Polygon Amoy or Ethereum Sepolia testnet.

Environment: Developed on Ubuntu Linux using Virtual Environments (venv) for clean dependency management.