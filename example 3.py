# practice for loop 
# ask user name and count each character
# "Harshit Vashisth"
# H = 1
# a = 2
# r = 1
# s = 3 
# h = 3
# i = 2
# t = 2
#   = 1
# V = 1 
name = input ("enter your name : ")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]