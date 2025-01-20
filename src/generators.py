from src.transactions import dic
import random

def filter_by_currency(m):
    return filter(lambda x: x["operationAmount"]["currency"]['code'] == 'USD', m)

test_dic = dic
gen = filter_by_currency(dic)
for i in gen:
    print(i)

def transaction_descriptions(m):
    return (x["description"] for x in m)

for transaction in transaction_descriptions(test_dic):
    print(transaction)

def card_number_generator(start: int, stop: int):
    for card_num in range(start, stop+1):
        if 1 <= start <= 9999999999999999 or 1 <= stop <= 9999999999999999:
            card_num = ''.join(f"{card_num:016}")
            num_str_formatted = ' '.join(card_num[k:k + 4] for k in range(0, 16, 4))
            yield num_str_formatted

gen = card_number_generator(55555550,55555555)
for i in gen:
    print(i)


