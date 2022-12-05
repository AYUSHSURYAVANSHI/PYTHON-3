# default parameters


# def user_info(first_name, last_name, age = None):  # we can made last input default parameter # **OR**
def user_info(first_name = None, last_name = None, age = None):
    print(f"Your first name is : {first_name}")  
    print(f"Your last name is : {last_name}")
    print(f"Your age is : {age}")


user_info('Ayush' , 'Suryavanshi' ,19)