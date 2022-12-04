name = "Ayush Suryavanshi"
# Ayush Suryavanshi 

# name.count("A") , name.count(name[0]) = 1
# name.count("y") , name.count(name[2]) = 2
# name.count("u") , name.count(name[3]) = 2
# name.count("s") , name.count(name[4]) = 2 
# name.count("h") , name.count(name[6]) = 2 
# name.count(" ") , name.count(name[7]) = 1
# name.count("S") , name.count(name[8]) = 1
# name.count("u") , name.count(name[9]) = 2 
# name.count("r") , name.count(name[0]) = 1 
# name.count("y") , name.count(name[10]) = 2 
# name.count("a") , name.count(name[11]) = 2
# name.count("v") , name.count(name[12]) = 1 
# name.count("a") , name.count(name[13]) = 2
# name.count("n") , name.count(name[14]) = 1
# name.count("s") , name.count(name[15]) = 2 
# name.count("h") , name.count(name[16]) = 2
# name.count("i") , name.count(name[17]) = 1
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
      temp_var + name[i]
      print(f"{name[i]} : {name.count(name[i])}")
      i += 1 


