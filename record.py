from name import Name
from phone import Phone

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        self.phone = Phone(phone)
        self.new_phone = Phone(new_phone)
        for i in range(len(self.phones)):
            if self.phones[i] == phone:
                self.phones[i] = new_phone

    def find_phone(self, phone):
        if phone in self.phones:
            return Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"
    
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# john_record.edit_phone("1234567890", "0987654321")
# john_record.find_phone("5555555555")
# print(f"{john_record.find_phone("5555555555")}")

# print(str(john_record))
