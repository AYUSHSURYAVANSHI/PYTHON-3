from functools import wraps

def only_data_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid arguments")
        return wrapper
    return decorator

@only_data_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string

print(string_join('harshit', 'vashisth', 'a' , 8))