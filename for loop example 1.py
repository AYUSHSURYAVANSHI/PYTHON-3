# sum from 1 to 10 
# 1 + 2 + 3 + 4 +............10

# total = 0  # 0 to 19
# for i in range(1,11):
#   total += i 
# print(total)


n = int(input("enter the numbber : "))
total = 0 
for i in range(1,n+1):
    total += i 
print(total)