square = (i**2 for i in range(1,11))


print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))


# for num in square:
#    print(num)

# for num in square:
#    print(num)


# GENERATOR VS LIST 
import time
# t1 = time.time()
# l = [i**2 for i in range (1000000000)] # 10 million 
# print(time.time() - t1)


t1 = time.time()
g = (i**2 for i in range(10000000000)) # 10 million 
print(time.time() - t1)