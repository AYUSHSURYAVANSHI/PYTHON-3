# create a laptop class with attributes like brand name , model name , price 
# create two objects/instance of your laptop class 


class laptop:
    def __init__(self,brand,model_name,price):
        # instance variable 
        self.brand = brand
        self.modal_name = model_name
        self.price = price 
        self.price_name = brand + ' ' + model_name

laptop1 = laptop('hp','au114tx',630000)
print(laptop1.brand)


