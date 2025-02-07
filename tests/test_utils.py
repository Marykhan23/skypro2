import json
from unittest.mock import Mock

from src.utils import import_transactions


def test_import_transactions(dic_parsed_transactions):
    mock_random = Mock(return_value=dic_parsed_transactions)
    json.loads = mock_random
    assert (
        import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations.json")
        == dic_parsed_transactions
    )
    mock_random.assert_called_once()


def test_import_transactions_no_transactions():
    mock_random = Mock(return_value=[])
    json.loads = mock_random
    assert import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations_empty.json") == []


def test_import_transactions_no_such_file():
    mock_random = Mock(return_value="Error <class 'FileNotFoundError'>")
    json.loads = mock_random
    assert (
        import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations_not_found.json")
        == "Error <class 'FileNotFoundError'>"
    )
