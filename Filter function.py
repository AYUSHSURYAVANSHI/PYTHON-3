# filter function

def is_even(a):
    return a%2 == 0


numbers = [3,4,5,6,7,8,9,10]
evens = []

filter(is_even, numbers)
print(filter(is_even, numbers))

# evens = tuple(filter(is_even, numbers))
evens = tuple(filter(lambda a:a%2==0, numbers))
# print(evens)

for i in evens:
    print(i)
print(list(evens))
# list comprehention 
new_evens = [i for i in numbers if i%2==0]



