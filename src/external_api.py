import os
import requests
from dotenv import load_dotenv
from src.utils import import_transactions

load_dotenv()

def calculate_transaction_sum(transaction, convert_to = "RUB"):
    """The function return amount and convert sum if foreign currency"""
    print(transaction)
    cur_code  = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if cur_code == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        headers = {
            'apikey': f'{os.getenv('API_LAYER_KEY')}'
        }
        r = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={cur_code}&amount={amount}",
                         headers = headers)

        return r.json()["result"]

tr = import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations.json")
print(calculate_transaction_sum(tr[1]))