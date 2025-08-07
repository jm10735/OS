import requests
from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

# Replace this with your actual contract address and ABI
contract_address = "0xYourContractAddressHere"
contract_abi = [...]  # <-- Paste ABI here

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

response = requests.get("http://localhost:5001/api/workday/employees")
employees = response.json()

for emp in employees:
    tx_hash = contract.functions.storeRecord(
        emp['id'], emp['name'], emp['title'], emp['start_date']
    ).transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Stored {emp['name']} on blockchain")
