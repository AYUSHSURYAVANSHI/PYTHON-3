n = int(input(" enter a number :"))
for i in range(0,n):
    for j in range(0,n):
        if i+j+1<=n-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()