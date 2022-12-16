# kwargs (keyword arguments)
# **kwargs (double star operator)
 
# kwargs as a parameter

def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v}")


# dictionary unpacking 
d= {'name':'Harshit','age': 19}
# func(first_name = 'harshit', last_name = 'Vashistha')
func(**d)






