class Phone:
    def __init__(self, brand,model_name,price):
        self.brand = brand 
        self.model_name = model_name
        self._price = max(price,0) 
        # if price > 0:
        #    self._price = price 
        # else:
        #    self._price = 0
        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self.price}"
 
    @property 
    def price(self):
        return self._price


    @price.setter 
    def price(self,new_price):
        self._price = max(new_price,0)
    # getter() , setter()
    def complete_specification(self):
        return f"{self.brand} {self.modal_name} and price is {self._price}"
   
    def make_a_call(self,Phone_number):
        print(f"calling {Phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}" 
Phone1 = Phone('nokia','1100',1000)
# print(phone1.brand)
# print(phone1.phone1.__price)
# print(phone1.__dict__)
# print(phone1.model_name)
Phone1._price = 500
print(Phone1.price)
print(Phone1.complete_specification)

