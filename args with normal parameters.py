# *args with normal parameters

def multiply_nums(num,*args):
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i 
    return multiply 

print(multiply_nums(1,2,3))