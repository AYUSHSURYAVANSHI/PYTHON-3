# def function
# input 

# num , iterable(tuple,list)containing numbers as args 

# example 
# nums = [1,2,3]
# to_power(3,*num)

# output 
# list -----> [1**3,8,27]

# if user didn't pass any args then give a user a message 'hey you didn't pass 
# args 

# else 
# return list 

# NOTE - USE list comprehension

def to_power(num,*args):
    if args:
        return ["i**num for i in args"]
    else:
        return "you didn't pass any args"

nums = [1,2,3]
print(to_power(2,*[3,4]))