from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import calculate_transaction_sum


@patch("requests.get")
def test_calculate_transaction_sum_if_usd(mock_get, dic_transactions_many):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1738495023, "rate": 98.624849},
        "date": "2025-02-02",
        "result": 810831.374823,
    }
    assert calculate_transaction_sum(dic_transactions_many[1]) == 810831.374823
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": "Abu9qUgNhWZYWMxepdgxWOm3PYnkNtzD"},
    )


def test_calculate_transaction_sum_if_rub(dic_transactions_many):
    assert calculate_transaction_sum(dic_transactions_many[0]) == 31957.58
