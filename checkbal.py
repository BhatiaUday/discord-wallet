import requests
import os

userwallet = "2QdhepnKRTLjjSqPL1PtKNwqrUkoLee5Gqs8bvZhRdMv"
tokenmint = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
rpc="https://bitter-newest-lake.solana-mainnet.discover.quiknode.pro/dc95a531b9b8cad9bf3084163513e413f54aa9f1/"

url = os.getenv("https://bitter-newest-lake.solana-mainnet.discover.quiknode.pro/dc95a531b9b8cad9bf3084163513e413f54aa9f1/")
headers = {"accept": "application/json", "content-type": "application/json"}

payload = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "getTokenAccountsByOwner",
    "params": [
        userwallet,
        {"mint": tokenmint},
        {"encoding": "jsonParsed"},
    ],
}
response = requests.post(rpc, json=payload, headers=headers)
data=response.json()["result"]["value"][0]["account"]["data"]["parsed"]["info"]["tokenAmount"]["uiAmount"]
print(data)
