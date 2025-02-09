import json

# import logging
from src.logger import utils_logger


def import_transactions(path):
    """The function take a path and return parsed data"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            utils_logger.info(f"Reading file {path}")
            data = file.read()
            parsed_data = json.loads(data)
        return parsed_data
    except Exception as e:
        utils_logger.error(f"{e.__class__} when reading the file {path}")
        return f"Error {e.__class__}"


tr = import_transactions("C:\\Users\\Maria\\PycharmProjects\\skypro1\\src\\data\\operations.json")
print(tr)
