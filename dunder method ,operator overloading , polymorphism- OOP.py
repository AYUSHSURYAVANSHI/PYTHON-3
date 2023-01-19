# special magic method / dunder method 
# operator overloading

class Phone:
    def __init__(self,brand, model,price):
        self.brand = brand 
        self.model = model 
        self.price = price 

    def phone_name(self):
        return f"{self.brand} {self.model}"


l = [1,2,3]
print(l)

my_phone = Phone('nokia','1100',1000)
print(my_phone)

# str,repr
def __str__(self):
    return f'{self.brand} {self.model}'

# def__str__(self):
#    return f'{self.brand} {self.model} and price is {self.price}'

# def__repr__(self):
#    return f'Phone(\'{self.brand}\',\'{self.model}\',{self.price})'

# print(str(my_Phone))
# print(my_Phone.__repr__())
s = (2,3,4)
print(len(l))
# print(len(s))
def __add__(self, other):
    return self.price + other.price

# Operater overloading

# my_Phone = Phone('nokia','1100',1000)
# my_Phone2 = Phone('nikia','1600',1200)
# print(my_Phone + my_Phone2) 

# polymorphism - method overriding

def phone_name(self):
    return f"{self.brand} {self.model}"

my_smartphone = smartphone('oneplus','5t',33000,'16MP')
print(my_smartphone)
print(my_smartphone.phone_name())
