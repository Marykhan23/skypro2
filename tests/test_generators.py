from src.generators import *
import pytest

def test_filter_by_currency_only_usd(dic_transactions, dic_transaction_only_usd):
    gen = filter_by_currency(dic_transactions, "USD")
    result_1 = next(gen)
    result_2 = next(gen)
    result_3 = next(gen)
    assert result_1 == dic_transaction_only_usd[0]
    assert result_2 == dic_transaction_only_usd[1]
    assert result_3 == dic_transaction_only_usd[2]

def test_filter_by_currency_no_usd(dic_transactions_no_usd, dic_transaction_only_usd):
    result = list(filter_by_currency(dic_transactions_no_usd, "USD"))
    assert result == []

def test_filter_by_currency_no_transactions():
    result = list(filter_by_currency([], "USD"))
    assert result == []

## Test transaction_descriptions
def test_transaction_descriptions(dic_transactions):
    gen = transaction_descriptions(dic_transactions)
    result_1 = next(gen)
    result_2 = next(gen)
    result_3 = next(gen)
    result_4 = next(gen)
    result_5 = next(gen)
    assert result_1 == "Перевод организации"
    assert result_2 == "Перевод со счета на счет"
    assert result_3 == "Перевод со счета на счет"
    assert result_4 == "Перевод с карты на карту"
    assert result_5 == ""

def test_transaction_descriptions_empty_list():
    result = list(transaction_descriptions([]))
    assert result == []

## Test card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (111, 112, ['0000 0000 0000 0111','0000 0000 0000 0112']),
    (0, 1,  ['0000 0000 0000 0000','0000 0000 0000 0001']),
    (9999999999999998,9999999999999999, ['9999 9999 9999 9998','9999 9999 9999 9999'])
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
