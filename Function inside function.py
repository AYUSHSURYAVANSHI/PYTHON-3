def greater(a,b):
    if a > b:
        return a 
    else:
        return b
num1 =int(input("enter first number"))
num2 =int(input("enter second number"))
bigger = greater(num1,num2)

print(f"{bigger} is greater ")

def greatest(a,b,c):
     if a > b:
       return a
     elif b>a and b>c:
       return b
     else: 
       return c

print(greatest(10,20,30))



def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
print(new_greatest(10,20,30))


# kiss - keep it simple stupid 

# function inside function 
# greater(a,b) -----> a or b 
# greater(a or b , c) --------> greatest
