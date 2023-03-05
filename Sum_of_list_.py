list=[[3,4,1],[5,7,4],[2,11,2]]
max=0
for i in list:
    sum=0
    for j in i:
        sum+=j
    if sum>max:
        max=sum
    else:
        max=max

print("Largest sum is", max)

print("Ayush Suryavanshi \n")
