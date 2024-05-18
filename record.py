from name import Name
from phone import Phone

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone, new_phone):
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.edit_phone("1234567890", "0987654321")
# john_record.find_phone("5555555555")
# print(f"{john_record.find_phone("5555555555")}")

# print(str(john_record))
