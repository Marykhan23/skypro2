def get_mask_card_number(card_number: str) -> str:
    """Masks card number to the format **XXX"""
    mask_card_number = card_number.replace(card_number[6:12], "******")
    card_num_with_spaces = ""
    for i in range(0, len(mask_card_number), 4):
        card_num_with_spaces += mask_card_number[i:i + 4] + " "
    card_num_with_spaces = card_num_with_spaces[:-1]
    return card_num_with_spaces


def get_mask_account(account_number: str) -> str:
    """Masks account number to the format XXXX XX** **** XXXX"""
    mask_account_number = account_number[-4::]
    return "**" + mask_account_number
