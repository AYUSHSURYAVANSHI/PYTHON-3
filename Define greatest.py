def greatest(a,b,c):
     if a > b:
       return a
     elif b>a and b>c:
       return b
     else: 
       return c

print(greatest(10,20,30))