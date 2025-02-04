from src.test_data.transactions import dic


def filter_by_currency(m: dic, cur):
    """Filter dictionaries with transactions by currency"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == cur, m)


gen = filter_by_currency(dic, "USD")
for i in gen:
    print(i)


def transaction_descriptions(m):
    """Filter dictionaries with transactions by description"""
    return (x["description"] for x in m)


# for transaction in transaction_descriptions(test_dic):
#     print(transaction)


def card_number_generator(start: int, stop: int):
    for card_num in range(start, stop + 1):
        if 1 <= start <= 9999999999999999 or 1 <= stop <= 9999999999999999:
            card_num = "".join(f"{card_num:016}")
            num_str_formatted = " ".join(card_num[k : k + 4] for k in range(0, 16, 4))
            yield num_str_formatted


# gen = card_number_generator(55555550,55555555)
# for i in gen:
#     print(i)
