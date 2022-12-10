# word counter
# harshit
# d = {'h': 2, 'a': 1, 'h':3}
# print(d)
 
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count 

print(word_counter("Harshit"))



