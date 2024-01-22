from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
            self.value = value
        else:
            raise ValueError

class Phone(Field):
     def __init__(self, value):
        if value.isnumeric() and len(value) == 10:
            self.value = value
        else:
            raise ValueError
            
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            new_phone = Phone(phone)
            self.phones.append(new_phone)    
        except ValueError:
            print('Wrong phone foramt!')

    def remove_phone(self, phone):
        phone_num = Phone(phone)

        for i in filter(lambda i: i.value == phone_num.value, self.phones):
            self.phones.remove(i)
    
    def edit_phone(self, old_phone, new_phone):
        old, new = Phone(old_phone), Phone(new_phone)

        for i in self.phones:
            if i.value == old.value:
                self.phones.remove(i)
                self.phones.append(new)
                return 'Phone number updated!'
            else:
                raise ValueError

    def find_phone(self, phone):
        phone_num = Phone(phone)

        for i in filter(lambda i: i.value == phone_num.value, self.phones):
            return phone_num

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        try:
            self.data[record.name.value] = record   
        except ValueError:
            print('Failed to add the record!')

    def find(self, name):
        return self.data[name] if name in self.data else None

    def delete(self, name):
        self.data.pop(name) if name in self.data else None

# тут додала ту перевірку з LMS
if __name__ == '__main__':
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
