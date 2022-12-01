# number1 = input(" enter first number ")
# number2 = input(" enter second number ")
# number3 = input(" enter third number  ")
number1,number2,number3 = input(" enter three numbers comma separated : ").split(",")
# (int(number1) + int(number2) + int(number3)) / 3
print(f"average of three numbers : {( int(number1) + int(number2) + int(number3)) / 3}")
