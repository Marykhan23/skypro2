import datetime
import time


def log(filename=""):
    def inner_decorator(function):
        def wrapper(*args, **kwargs):
            log_time = datetime.datetime.now()
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(f"{filename}.txt", 'a') as file:
                        file.write(f"{log_time} {function.__name__} OK\n")
                else:
                    print(f"{log_time} {function.__name__} OK\n")
                return result
            except Exception as e:
                if filename:
                    with open(f"{filename}.txt", 'a') as file:
                        file.write(f"{log_time} {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{log_time} {function.__name__} error: {e}\n")
                raise e
        return wrapper
    return inner_decorator

@log("log1")
def divide_number(x, y):
    return x/y

try:
    divide_number(3, 0)
except Exception as e:
    print(e)
time.sleep(3)

try:
    divide_number(3, "u")
except Exception as e:
    print(e)
time.sleep(3)
divide_number(3, 1)
