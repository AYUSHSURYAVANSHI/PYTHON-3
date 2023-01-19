# Encapsulation 

class phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand 
        self.model_name = model_name
        self.__price = price 

# l = [3,4,5,6]
# l.sort()
# print(l)
    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_mesaage(self):
        pass # teilio 

phone1 = phone('nokia','1100',1000)
# print(phone1.__price)
print(phone1.phone1.__price)
print(phone1.__dict__)

phone1.__price = -1000
print(phone1._price)

