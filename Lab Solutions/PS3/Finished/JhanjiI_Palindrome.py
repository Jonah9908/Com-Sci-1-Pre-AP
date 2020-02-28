# Ishaan Jhanji
# Palindrome.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

words = ["radar", "banana", "alababa", "Hannah", "racecar"]

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

spot = 0
word = ""

while spot < len(words):
    word = words[spot]
    word = word.upper()
    if word == word[ : : -1]:
        print "PALINDROME"
    else :
        print "just a word"
    spot = spot + 1
