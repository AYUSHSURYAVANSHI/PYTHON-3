# Dictionary comprehension

# square = {1:1,2:4,3:9}
square = {num:num**2 for num in range(1,11) }
print(square)

square = {f"Square of {num} is":num**2 for num in range(1,11) }
print(square)  

for k,v in square.items():
    print(f"{k} : {v}")

string = "Harshit"
for i in string:
    print(i)

# {'H': 1,'a' : 1}
word_count = {char:string.count(char) for char in string}

print(word_count)






