from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value]=record

    def find(self, name):
        for name, record in self.data.items():
            if name in name:
                return record

    def delete(self, name):
        if self.find(name):
            del self.data[name]