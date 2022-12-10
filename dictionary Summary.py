# summary dictionary 
# what is dictionary 
# unordered collection of data 

d = {'name' : 'harshit', 'age' : 24 }
# Or
d = dict(name = 'harshit', age = 24)

# Or

d2 = {
    'name' : 'harshit',
    'age' : 24,
    'Fav_movies' : []

}

# how to access data from dictionary
# you cannot do like 
# d[0], because there is no order inside dictionary 
# 
# syntex
# print(dictname[keyname])
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] =  'value2'
print(empty_dict) 

# check existence of values inside dict 
# use in keyword to check for keys 
if 'name' in d:

# how to iterate over dictionary 

# most commen method 
 for key , value in d.items():
    print(f'key is {key} and value is {value}')

# to print all keys 
 for i in d:
     print(i)

# most common dict methods 
# to access a key and check existance
# d.get('name')  

# Q - why we use get 
# A - to get rid of error
# example 
# print(d['names'])
# print(d.get('names'))


# to delete item 
# pop -----> take one argument which is keyname 

# popped = d.pop(name)
# print(popped)   
# print(d)

# popitem 
popped = d.popitem()
print(popped)

# example
# print(d['names'])
# print(d.get('names'))
