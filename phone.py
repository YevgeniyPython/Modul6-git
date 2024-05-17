from field import Field

class Phone(Field):
    def __init__(self, phone: str):
        # another method
        # x = filter(str.isdecimal, phone)
        # check_phone = "".join(x)
        check_phone = "".join(x for x in phone if x.isdecimal())
        assert len(check_phone)==len(phone)==10, f"phone should include 10 digits"
        self.phone = phone

    def __str__(self):
        return str(self.phone)

# phone1 = Phone("1234567890")
# print(phone1.phone)
