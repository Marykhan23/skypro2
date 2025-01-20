from src.masks import *

## tests for get_mask_card_number
def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

def test_get_mask_card_number_when_empty():
    assert get_mask_card_number('') == 'No card number'

def test_get_mask_card_number_when_space():
    assert get_mask_card_number(' ') == 'No card number'

def test_get_mask_card_number_when_trailing_space():
    assert get_mask_card_number('          7000792289606361     ') == '7000 79** **** 6361'

def test_get_mask_card_number_when_text():
    assert get_mask_card_number('Card number 7000792289606361') == '7000 79** **** 6361'

def test_get_mask_card_number_when_only_text():
    assert get_mask_card_number('Card number c55') == 'No card number'

def test_get_mask_card_number_when_less_than_16_digits():
    assert get_mask_card_number('700079229606361') == 'Wrong card number format'

def test_get_mask_card_number_when_more_than_16_digits():
    assert get_mask_card_number('700079229606361') == 'Wrong card number format'

## test for get_mask_account
def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'

def test_get_mask_account_when_empty():
    assert get_mask_account('') == 'No account number'

def test_get_mask_account_when_space():
    assert get_mask_account(' ') == 'Wrong account number format'

def test_get_mask_account_when_trailing_space():
    assert get_mask_account('          73654108430135874305     ') == '**4305'

def test_get_mask_account_when_text():
    assert get_mask_account('Account number 73654108430135874305') == '**4305'

def test_get_mask_account_when_only_text():
    assert get_mask_account('Account number c55') == 'Wrong account number format'

def test_get_mask_account_when_less_than_20_digits():
    assert get_mask_account('736541084301358743051') == 'Wrong account number format'

def test_get_mask_account_when_more_than_20_digits():
    assert get_mask_account('7365410843013587430') == 'Wrong account number format'


