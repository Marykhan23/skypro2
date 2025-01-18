import src.masks as masks
from datetime import datetime


def mask_account_card(number: str) -> str:
    """Masks card or account number in any strings"""
    res = ""
    for i in number.split(" "):
        if i.isdigit():
            if len(i) == 20:
                i = masks.get_mask_account(i)
            elif len(i) == 16:
                i = masks.get_mask_card_number(i)
        res += i + " "
    res = res[:-1]
    return res


def get_date(date: str) -> str:
    """Converts datetime string to dd.mm.YYYY format"""
    try:
        datetime_formatted = datetime.fromisoformat(date)
        print("datetime_formatted = " + str(datetime_formatted))
        date_formatted = (
                datetime_formatted.strftime("%d")
                + "."
                + datetime_formatted.strftime("%m")
                + "."
                + datetime_formatted.strftime("%Y")
        )
        return date_formatted
    except ValueError:
        return "Invalid data"
