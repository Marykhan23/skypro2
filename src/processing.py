from typing import List

def filter_by_state(dics: List[dict], state: str = 'EXECUTED') -> List[dict]:
    """Returns list of dictionaries filtering by state"""
    new_dict = []
    for i in dics:
        if i['state'] == state:
            new_dict.append(i)
    return new_dict


def sort_by_date(dics: List[dict], reverse: bool=True) -> List[dict]:
    """Returns sorted list of dictionaries by Date"""
    list_sorted = []
    list_sorted = sorted(dics, reverse=reverse, key = lambda x: x.get('date'))
    return list_sorted