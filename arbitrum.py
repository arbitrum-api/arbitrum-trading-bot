import requests
import json

# API URL
API_URL = "https://arbitrum-api.co/api/v1"

# Function to transfer tokens
def transfer_token(from_address, to_address, amount, token_address, private_key):
    url = f"{API_URL}/transfer"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "from": from_address,
        "to": to_address,
        "amount": str(amount),  # It's important to send amount as a string
        "token": token_address,
        "private_key": private_key
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to get token balance
def get_token_balance(address, token_address):
    url = f"{API_URL}/token-balance"
    params = {
        "address": address,
        "token": token_address
    }
    response = requests.get(url, params=params)
    return response.json()

# Example usage
if __name__ == "__main__":
    from_address = "0xYourSenderAddressHere"
    to_address = "0xReceiverAddressHere"
    amount = 10  # Amount to send
    token_address = "0xTokenAddressHere"  # Token address (e.g., USDT token)
    private_key = "0xYourPrivateKeyHere"  # Sender's private key

    # Transfer tokens
    transfer_result = transfer_token(from_address, to_address, amount, token_address, private_key)
    print("Transfer Result:", transfer_result)

    # Get token balance
    balance_result = get_token_balance(from_address, token_address)
    print("Balance Result:", balance_result)
