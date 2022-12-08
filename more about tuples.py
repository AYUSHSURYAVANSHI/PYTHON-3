# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking 
# list inside tuple 
# some functions that you can use with tuples 
 
mixed = (1,2,3,4.0)

# for loop and tuple 
for i in mixed:
    print(i)
# NOTE - you can use while loop too 

# tuple with one element 
# nums = (1,)
# words = ('word1',)
# print(type(nums))
# print(type(words))


# tuple without parenthesis 
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# tuple unpacking 
guitarsts = ('Maneli Jamal','Eddie Van Der Meer', 'Andrew Foy')
guitarst1,guitarst2,guitarst3 = (guitarsts)
print(guitarst1)
print(guitarst2)
print(guitarst3)


# list inside tuples
favorites =('southern magnolia',['Tokyo Ghoul Theme','landscape'])
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

# min(), max(), sum 
print(min(mixed))
print(max(mixed))
print(sum(mixed))




