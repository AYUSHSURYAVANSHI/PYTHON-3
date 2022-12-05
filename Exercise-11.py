# def is_palindrom(word):
#    reversed_word = word[::-1]
#    if word == reversed_word:
#        return True 
#    else:
#        return False

# def is_palindrom(word):
#    if word ==  word[::-1]:
#        return True 
#   return False

def is_palindrom(word):
   return word == word[::-1]

print(is_palindrom("naman"))
print(is_palindrom("horse"))
    





