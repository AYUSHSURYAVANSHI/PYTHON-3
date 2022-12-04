winning_number = 20
user_input = input("guess a number between 10 to 100 : ")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN!!!!")

else: #nested if else 
     if user_input < winning_number:
         print("too low")
     else: 
        print("too high ")    
       
