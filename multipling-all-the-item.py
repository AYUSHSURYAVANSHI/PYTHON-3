def multiplyvalue(dictionary):
        multy=1
        for i in dictionary :
            multy*=int(dictionary[i])
        return multy

dictionary={"one":1,"three":3,"seven":7,"fifteen":15,"ten":10}

print("Multiply of all values is :", multiplyvalue(dictionary))

print("Ayush Suryavanshi \n")

