from src.logger import masks_logger


def get_mask_card_number(card_number: str) -> str:
    """Masks card number to the format **XXX"""
    mask_card_number = ""
    masks_logger.info("Start searching for the card")
    for i in card_number.strip().split(" "):
        if i.isdigit():
            mask_card_number = i.strip().replace(i[6:12], "******")
    if not mask_card_number:
        masks_logger.error(f"Couldn't find a card number in \"{card_number}\"")
        return "No card number"
    elif len(mask_card_number) != 16:
        masks_logger.error(f"Wrong card format in \"{card_number}\"")
        return "Wrong card number format"
    card_num_with_spaces = ""
    for i in range(0, len(mask_card_number), 4):
        card_num_with_spaces += mask_card_number[i : i + 4] + " "
    card_num_with_spaces = card_num_with_spaces[:-1]
    masks_logger.info(f"Found card number {card_num_with_spaces}")
    return card_num_with_spaces


def get_mask_account(account_number: str) -> str:
    """Masks account number to the format XXXX XX** **** XXXX"""
    mask_account_number = ""
    masks_logger.info("Start searching for account")
    for i in account_number.strip().split(" "):
        if i.isdigit():
            account_number = i
    if not account_number:
        masks_logger.error(f"Couldn't find an account number in \"{account_number}\"")
        return "No account number"
    elif len(account_number) != 20:
        masks_logger.error(f"Wrong account number format in \"{account_number}\"")
        return "Wrong account number format"
    mask_account_number = "**" + account_number[-4::]
    masks_logger.info(f"Found account number {mask_account_number}")
    return mask_account_number

get_mask_card_number("fgdf MasterCard  xcb sdfgdf")
get_mask_account("Счет 64686473678894779589")