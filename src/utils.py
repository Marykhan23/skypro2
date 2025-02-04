import json

def import_transactions(path):
    """The function take a path and return parsed data"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
            parsed_data = json.loads(data)
        return parsed_data
    except Exception as e:
        return(f"Error {e.__class__}")

tr = import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations4.json")
print(tr)

