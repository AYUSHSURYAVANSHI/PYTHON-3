# defind a function that list of strings 
# list containing reverse of every string 

# NOTE - USE LIST COMPREHENSION BECAUSE we alreadydid this execise 
# using normal method 

# Exemple 
# l = ['abc','tuv','xyz']
# reverse_string(1) -------> ['cba','vut','zyx']

# reverse string 
# l = input("enter a name :")
# def reverse_strings(l):
#    return [name[::-1] for name in l ]
#
# print(reverse_strings([l]))


def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list
print(reverse_str(['abc','tuv','xyz']))


