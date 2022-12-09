# in keyword and iterations in dictionary.py

user_info = {
    'name' : 'harshit',
    'age' : 24,
    'fev_movies' : ['coco', 'kimi no na wa'],
    'fev_tunes' : ['awekening','fairy tale'],
}
 


# check if key exist in dictionary  
# if 'name' in user_info:
#     print('present')
# else:
#       print('not present')
# check if value exist in dictionary
# if 'harshit' in user_info:
#    print('present')
# else:
#    print('not present')


# check if value exist in dictionary ----> values method 

if 24 in user_info.values():
    print('present')
else: 
    print('not present')

# loops in dictionaries 
for i in user_info:
    print(i)

# values method 
user_info_values = user_info.values()
print(user_info_values) 
print(type(user_info_values))

user_info_values = user_info.keys() 

print(user_info.keys)
print(type(user_info.keys)) 

# loops in dictionaries    
for i in user_info:   
      print(user_info[i]) 

# items method 
user_items = user_info.items()
print(user_items)
print(type(user_items))

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")



