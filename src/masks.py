def get_mask_card_number(card_number: str) -> str:
    """Masks card number to the format **XXX"""
    mask_card_number = ''
    for i in card_number.strip().split(" "):
        if i.isdigit():
            mask_card_number = i.strip().replace(i[6:12], "******")
    if not mask_card_number:
        return "No card number"
    elif len(mask_card_number) != 16:
        return "Wrong card number format"
    card_num_with_spaces = ""
    for i in range(0, len(mask_card_number), 4):
        card_num_with_spaces += mask_card_number[i:i + 4] + " "
    card_num_with_spaces = card_num_with_spaces[:-1]
    return card_num_with_spaces


def get_mask_account(account_number: str) -> str:
    """Masks account number to the format XXXX XX** **** XXXX"""
    mask_account_number = ''
    for i in account_number.strip().split(" "):
        if i.isdigit():
            account_number = i
    if not account_number:
        return "No account number"
    elif len(account_number) != 20:
        return "Wrong account number format"
    mask_account_number = account_number[-4::]
    return "**" + mask_account_number
