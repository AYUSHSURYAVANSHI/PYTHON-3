num = int(input("enter a number"))
if num >2:
    for i in range(2,num):
        if( num % i ==0):
            print("number is positive :")
            break
        else:
            print("number is not positive :")
            break
else:
    print("number is positive ")


    