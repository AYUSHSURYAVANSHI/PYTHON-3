from functools import wraps 

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper
# print add(a,b)
def add(a,b):
    '''this function takes two numbers as argumnets and return their sum'''
    return a+b 



print(add(4,5))
