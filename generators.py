# generators are iterators
l = [1,2,3,4,]
for num in map(lambda a :a**2,l):
    print(num)


# memory -----[------------------------------], list 
# memory -----(9)



# create your first generator with generator function 
# 1.) generator function

# 10 , 1 to 10 

def nums(n):
    for i in range(1,n+1):
        yield(i)
for number in nums(10):
    print(nums(10))



