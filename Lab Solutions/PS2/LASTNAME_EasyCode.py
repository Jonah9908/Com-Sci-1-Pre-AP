# Ishaan Jhanji
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

editSentence = []
beforeChange = ""
newWord = ""
spot = 0
newSentence = ""
upper = ""
upperWord = ""

while spot< len(sentence):
    beforeChange = sentence[spot]
    newWord = beforeChange[0:(len(beforeChange)+1):2]
    newWord = str(newWord) + str(beforeChange[1:(len(beforeChange)+1):2])
    if spot == 0:
        upperWord = sentence[0]
        upper = upperWord[0]
        upper = upper.upper()
        newWord = upper + newWord[1::]
    newSentence = str(newSentence) + " " + str(newWord)
    spot = spot + 1

print (newSentence + ".")

