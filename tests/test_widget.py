import pytest

from src.widget import get_date
from src.widget import mask_account_card


## tests for mask_account_card
@pytest.mark.parametrize(
    "data, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Account number 73654108430135874305", "Account number **4305"),
        (
            "Card number 7000792289606361 Account number 73654108430135874305",
            "Card number 7000 79** **** 6361 Account number **4305",
        ),
        ("", ""),
        (" ", " "),
        ("  Card number ", "  Card number "),
        ("././.56", "././.56"),
        ("7365410843013587430", "7365410843013587430"),  # less than 20
        ("736541084301358743011", "736541084301358743011"),  # more than 20
        ("159683786870519", "159683786870519"),  # less than 16
        ("15968378687051990", "15968378687051990"),  # more than 16
    ],
)
def test_mask_account_card_with_parameters(test_data, expected):
    assert mask_account_card(test_data) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("", "Invalid data"),
        (" ", "Invalid data"),
        ("ghfghfgh", "Invalid data"),
        ("20221227", "27.12.2022"),
        (".....", "Invalid data"),
    ],
)
def test_get_date_with_parameters(test_data, expected):
    assert get_date(test_data) == expected
