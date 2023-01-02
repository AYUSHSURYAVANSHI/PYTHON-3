# decorators - enhance the functionality of other functions

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function 



# this is awesome function
@decorator_function # shortcut  
def func1():
    print('this is function 1')
@decorator_function # shortcut 
def func2():
    print('this is function 2')

# this is awesome function 
func1 = decorator_function(func1)
func1()
func2 = decorator_function(func2)
func2()

