# iterator vs iterables 

numbers = [1,2,3,4] #, tuples,string ---- # iterables
squares = map(lambda a:a**2, numbers) # iterator 


# for i in numbers:
#   print(i)


# step call iter function

# iter(numbers) ----> iterator 
# next(iter(numbers))
# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# iterator 

next(squares)
print(next(squares))
print(next(squares))
print(next(squares))


