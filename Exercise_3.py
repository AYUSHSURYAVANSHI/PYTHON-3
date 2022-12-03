#take two comma separated inputs from user 
name,char = input("enter comma seperated name and character : ").split(",")
print(f"lenght of your name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}") # case sensitive 
# Harshit - harshit
# H - h
# " Harshit ".......> "Harshit" ........> "harshirt"
# "  H " ........> "h" ...........> "h"
#name.strip().lower().count(char.strip().lower())
#char.strip().lower()
