from field import Field

class Name(Field):
    def __init__(self, value):
        self.value = value

# name1 = Name("Q")
# print(name1.name)
# print(str(name1))    