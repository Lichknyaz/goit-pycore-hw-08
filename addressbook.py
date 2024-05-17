from collections import UserDict
from datetime import datetime
from custom_errors import InvalidDateFormatError
import pickle



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
	pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10:
            raise ValueError
    def __repr__(self):
        return f"{self.value}"
        
class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise InvalidDateFormatError



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        p = Phone(phone)
        self.phones.append(p)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

        
    def delete_phone (self, phone):
        for p in self.phones:
             if p.value == phone:
                  self.phones.pop(p)

    def edit_phone (self, phone, new_phone):
         for p in self.phones:
              if p.value == phone:
                   p.value = new_phone
                          
    def find_phone (self, phone):
         for p in self.phones:
              if p.value == phone:
                   return phone
                      

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
        
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        self.data.pop(name)

    def find(self, name):
        if name in self.data:
            return self.data[name]
        
    def save_data(book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)

    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()
    
    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    

