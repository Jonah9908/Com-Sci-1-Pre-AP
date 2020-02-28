# Jonah Sims
# EasyCode.py  

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
sentence = ["this", "is", "a", "test", "of", "the", "emergency", "broadcast", "system"]
'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''
spot = 0
code = ""

#print (code)

def word1(word):
    if len(word) < 2:
        return word
    return word[::2] +word[1::2]

for num in sentence:
    sentence[spot] = word1(sentence[spot])
    spot += 1
sentence[0] = sentence[0][0].upper() + sentence[0][1::]

spot = 0
while len(sentence) -1 > spot:
    code = code + sentence[spot] + " "
    spot = spot + 1
code = code + sentence[- 1] + "."
print(code)
