# list inside list

matrix = [[2,3,4],[2,6,7],[9,0,8]]
# 3 items ---> 3 list 
print(matrix[2])
for sublist in matrix:
     for i in sublist:
         print(i) 

print(matrix[2][0])

# find object type
# s = "string"
# print(type(s)) # string
# print(type(matrix)) # list 




