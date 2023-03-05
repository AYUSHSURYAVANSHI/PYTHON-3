def sumvalue(dictionary):
    sum=0

    for i in dictionary :
        sum+=int(dictionary[i])
    return sum

dictionary={"one":1,"thirty":30,"seven":7,"fifteen":15}

print("Sum of values are :", sumvalue(dictionary))

print("Ayush Suryavanshi \n")