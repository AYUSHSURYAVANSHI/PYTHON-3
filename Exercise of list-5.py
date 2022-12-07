# common elements finder function 
# define a functions which take 2 lists as input and return a list 
# which contains common element of both lists 

# example 
# input -----> [1,2,5,8] , [1,2,7,6]

# filter common elements
 
def common_finder(l1,l2):
    output = []
    for i in l1:
        if i in l2:
           output.append(i)
    return output 

common_finder([1,2,5,8],[1,2,7,6]) 
print(common_finder([1,2,5,8],[1,2,7,6]))



