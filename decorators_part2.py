from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print('this is awesome function')
        any_function(*args,**kwargs)
    return wrapper_function 

@decorator_function # shortcut  
def func():
    print(f'this is function with argument')

def add(a,b):
    return a + b 
print(add.__doc__)
print(add.__dpc__)