l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

l = [(1,2)(3,4)(5,6)(7,8)(9,10)]
# * operator with zip 
new_list = []
print(list(zip(*l)))

l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))

# for pair in zip(l1,l2):
#    new_list.append(max(pair))

# print(new_list)




