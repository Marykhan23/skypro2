from typing import List

def filter_by_state(dics: List, state = 'EXECUTED') -> List:
    """Returns list of dictionaries filtering by state"""
    new_dict = []
    for i in dics:
        if i['state'] == state:
            new_dict.append(i)
    return new_dict

#dic1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
#print(filter_by_state(dic1, 'CANCELED'))