# Object Oriented Programming 

# Comman Topic in almost all popular programming languages(ptyhon , java, c++)
# with comman idea but with different syntex 

# OOP is just style/way to write a code 

# very helpful in creating real world programs 

# we will see other advantages when we will start learning OOP

# create class 

class person:
    def __init__(self,first_name,last_name,age):
        # instace variables 
        print('init method called')
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 


p1 = person('Harshit','suryavanshi',24)
p2 = person('mohit','jain',22)

print(p1.first_name)
print(p2.first_name)
