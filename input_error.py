from custom_errors import InvalidDateFormatError

def input_error_change(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone from the database to change please."
        except KeyError:
            return "No such name in the database, give me valid name please"
    return inner


def input_error_add(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone please."
    return inner


def input_error_show(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone from the database to change please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Give me name from database please."
    return inner


def input_error_show_birthday(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name from the database please."
        except AttributeError:
            return "No birthday recorded, please add birthday"
    return inner


def input_error_add_birthday(func):
    def inner(*args):
        try:
            return func(*args)
        except InvalidDateFormatError:
            return "Invalid date format. Use DD.MM.YYYY"
        except ValueError:
            return "Give me name from the database and birthday to add please."
        except AttributeError:
            return "Give me name from database please"
    return inner



