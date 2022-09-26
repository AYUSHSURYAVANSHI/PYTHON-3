n=5
px=n
py=n
for x in range(1,n+1):
      for y in range(1,n*2):
        if y==px or y==py or x==n: 
            print("x",end="")
    else:
        print(" ",end="")
py-=1
py+=1
 print()

