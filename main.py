from functools import wraps
from addressbook import AddressBook, Record
from input_error import input_error_change, input_error_add, input_error_show, input_error_show_birthday, input_error_add_birthday
from datetime import datetime, timedelta


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error_change
def change_contact(args, book: AddressBook):

    name, phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(phone, new_phone)
    message = "Phone updated."
    return message
    

@input_error_add
def add_contact(args, book: AddressBook):

    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error_show
def show_phone (args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    phone = record.phones
    return phone

def show_all (book: AddressBook):
    for name, record in book.data.items():
        if record.birthday:
            b = record.birthday.value.strftime('%d.%m.%Y')
            print( "".join(f"Name: {name}, Phone Numbers: {str(record.phones)}, Birthday: {b}"))
        else:
            print( "".join(f"Name: {name}, Phone Numbers: {str(record.phones)}"))

@input_error_show_birthday
def show_birthday (args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    b = record.birthday.value.strftime('%d.%m.%Y')
    return  "".join(f"Name: {name}, Birthday: {b}")



@input_error_add_birthday
def add_birthday (args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return "Birthday added"


def get_upcoming_birthdays (book: AddressBook):
    upcoming_birthdays_list = []

    for name, record in book.data.items():
        if record.birthday != None:
            b = record.birthday.value
            birthday = datetime(year = datetime.now().year, \
                                month = b.month, \
                                day = b.day)
            days_till_birthday = birthday.toordinal() - datetime.now().toordinal()
            if days_till_birthday < 0:
                continue
            elif days_till_birthday <=7:
                if birthday.weekday() == 5:
                    congratulation_date = birthday + timedelta (days=2)
                    upcoming_birthdays_list.append ({"Name" : name, "congratulation_date": congratulation_date.strftime("%d.%m.%Y")})
                elif birthday.weekday() == 6:
                    congratulation_date = birthday + timedelta (days=1)
                    upcoming_birthdays_list.append ({"Name" : name, "congratulation_date": congratulation_date.strftime("%d.%m.%Y")})
                else:
                    upcoming_birthdays_list.append ({"Name" : name, "congratulation_date": birthday.strftime("%d.%m.%Y")})

    for item in upcoming_birthdays_list:
        print(f"Name: {item["Name"]}, Congratulation date: {item["congratulation_date"]}")


def main():
    book = AddressBook.load_data()
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "all":
            show_all(book)
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            get_upcoming_birthdays(book)
            
        else:
            print("Invalid command.")

    AddressBook.save_data(book)
if __name__ == "__main__":
    main()
