# defind a function which will take list containing numbers as input 
# and return list containing square of every elements

# example 
# number =[1,2,3,4]
# square_list(numbers) -----> return -----> [ 1,2,9,16]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)  
    return square
numbers = list(range(1,11))
# square_list(numbers)
print(square_list(numbers))