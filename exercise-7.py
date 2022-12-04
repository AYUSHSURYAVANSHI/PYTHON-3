number =input("enter a number ")
i = 0 
int(number[i])
# int(number[1])
# int(number[2])
# int(number[3])
# print("number")
# print(f"int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])")
total = 0
while i < len(number):
    total += int(number[i])
    i += 1
    print(total)
      
    