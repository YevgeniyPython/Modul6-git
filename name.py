from field import Field

class Name(Field):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return str(self.name)

# name1 = Name("Q")
# print(name1.name)
# print(str(name1))    