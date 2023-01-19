class laptop:
    def __init__(self,brand,model_name,price):
        # instance variable 
        self.brand = brand
        self.modal_name = model_name
        self.price = price 
        self.price_name = brand + ' ' + model_name
    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price 
        return self.price - off_price

laptop1 = laptop('hp','au114tx',63000)
laptop2 = laptop('apple','macbook pro',113000)
print(laptop2.apply_discount(10))

