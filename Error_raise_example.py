# raise errors Example 
# NotImplemented  Error 
# abstract method

class Animal:
    def __init__(self,name):
        self.name = name 

    def Sound(self):
        raise NOtImplementedError("you have this method in subclasses")

    def Sound(self):
        return "this is Animal Sound "
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed 

class cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed 

doggy = Dog('boony','pug')
print(doggy.Sound())

