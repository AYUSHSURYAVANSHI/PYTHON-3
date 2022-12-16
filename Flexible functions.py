# flexible function
# *operator
# *args

def total(a,b):
    return a+b
total(3,4)
print(total(3,4))

# def all_total(*args):
#     print(type(args))
#    
#all_total(1,2,3,4,5,65)

def all_total(*args):
    # (1,2,3,4,5,65)
    total = 0
    for num in args:
        total += num
    return total 

print(all_total(1,2,3,))