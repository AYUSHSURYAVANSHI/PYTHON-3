class person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    @classmethod 
    def from_string(cls,string):
       first,last,age = string.split(',')
       return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f" You have created {cls.count_instance} instances of person class"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age>18
p1 = person('Harshit','vashisth', 23)
p2 = person('Harshit','vashisth', 23)
p3 = person('Harshit','vashisth', 23)

p3 = person.from_string('Harshit,Vashisth,24')
print(p3.full_name())