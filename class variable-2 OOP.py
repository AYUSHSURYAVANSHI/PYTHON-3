class circle:
    pi = 3.14 
    def __init__(self,radius):
        self.radius = radius

    def calc_circumference(self):
        return 2*circle.pi*self.radius


c = circle(2)
c1 = circle(3)
print(c.calc_circumference())

# class variable 
class laptop:
    discount_percent = 10
    def __init__(self,brand,model_name,price):
        # instance variable 
        self.brand = brand
        self.modal_name = model_name
        self.price = price 
        self.laptop_name = brand + ' ' + model_name
    def apply_discount(self):
        # self.price
        off_price = (self.discount_percent/100)*self.price 
        return self.price - off_price

laptop1 = laptop('hp','au114tx',63000)
laptop2 = laptop('apple','macbook pro',230000)

laptop2.discount_percent = 50
print(laptop1.apply_discount())
print(laptop2.apply_discount())
print(laptop2.__dict__)
