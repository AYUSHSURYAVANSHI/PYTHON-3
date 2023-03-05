list=[[3,6,2],[7,9,3],[6,10,8]]
max=0
for i in list:
    sum=0
    for j in i:
         sum+=j 
    if sum>max:
        max=sum
    else:
        max=max

print("Largest sum is",max)

print("Ayush Suryavanshi\n")

