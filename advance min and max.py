# advance min and max 

numbers = [1,2,3,4,5,6]
print(max(numbers))

def func(item):
    return len(item)

names = ['Harshit','Mohit','ab']
print(max(names,key = lambda item : len(item)))

students ={
    'harshit': {'score': 90, 'age' : 24},
    'mohit' : {'score': 75, 'age' : 19},
    'rohit' : {'score': 76, 'age' : 23},
}

print(max(students,key = lambda item: students[item]['score']))

# students2 = [
#    {'name': 'harshit', 'score' : 90, 'age': 24},
#    {'name': 'mohit', 'score' : 70, 'age': 19},
#    {'name': 'rohit', 'score' : 60, 'age': 23},
# ]   
# print(max(students2,key = lambda item:item.get('score'))['name'])


