# add and delete data 
user_info = {
    'name' : 'harshit', 
    'age'  : ['coco','kimi no na wa'],
    'fev_movies' : ['coco','kimi no na wa'],
    'fev_tunes' : ['awakening', 'fairy tale']
}

# how to add data 
user_info['fev_songs'] = ['song1','song2']
print(user_info['fev_songs'])


# pop method
popped_item = user_info.pop('fev_movies')
print(f" popped item is {popped_item}")
print(type(popped_item))
print(user_info)


# popitem method 
popped_item = user_info.popitem()
print(user_info.popitem()) 
print(type(user_info.popitem()))





