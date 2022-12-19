# THIS IS CHALLANGE 

# defind a function take any no of lists containing numbers 
# [1,2,3],[4,5,6],[7,8,9]
# return average 
# (1+4,7)/3, (2,5,8)/3 , (3,6,9)/3

# try to make anonymous function in one line using lambda
 
# def average_finder(*args):
#    average = []
#    for pair in zip(*args):
#       average.append(sum(pair)/len(pair)) 
#    return average 

average_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(average_finder([1,2,3],[4,5,6],[7,8,9]))


# args = ([], [])







