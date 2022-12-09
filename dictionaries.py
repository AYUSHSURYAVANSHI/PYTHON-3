# Dictionaries intro 
# Q - why we use dictionaries ?
# A - Because of limitation of lists , lists are not enough to represent 
# real data . 

# Example 
# user = ['harshit', 24, ['coco', 'kimi no na wa'],['awekening','fairy tale']]
# this list contains user name , age , fev tunes 
# you can do this but this is not a good way to do this.

# Q - what are dictionaries 
# A - unordered collections of data in kay : value pair.


# how to create dictionaries 
# user = {'name': 'Harshit', 'age' : 24}
# print(user)
# print(type(user))

# second method to create dictionary 
# user1 = dict(name = 'Harshit',age = 24)
# print(user1)

# how to access data from dictionary 
# NOTE - There is no indexing because of unorderd collections of data.
# print(user['name'])
# print(user['age'])


# which type of data a dictionary can store ?
# anything 
# numbers, string, list, dictionary   

user_info = {
     'name' : 'harshit',
    'age' : 24,
    'fev_movies' : ['coco', 'kimi no na wa'],
    'fev_tunes' : ['awekening','fairy tale'],
}
print(user_info['fev_movies'])
print(user_info['fev_tunes'])





# How to add dat to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
user_info2['age'] = 12
print(user_info2)


 



