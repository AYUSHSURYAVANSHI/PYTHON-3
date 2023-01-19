# instance methods
l = [1,2,3]
l.pop()
class person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 

    def full_name(self):
        return f"{self.first_name} {self.last_name}"    
    def is_above_18(self):
        return self.age>18

p1 = person('Harshit','Vashistha',24)
p2 = person('Harsh','Varma',22)
# print(p2.full_name())
print(p1.is_above_18())
# print(person.full_name(p2))

l = [1,2,3]
# list.clear(l)
# print(l)
list.append(l,10)
print(l)
p1 = person('Harshit','Vashistha',24)

