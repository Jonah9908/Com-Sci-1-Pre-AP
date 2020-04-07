# First Last
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

def reverse(word):
    spot = len(word) - 1
    new_word = ""
    for num in len(word):
        new_letter = word[spot]
        new_word = new_letter + new_word
        spot -= 1
    return new_word


print(reverse("hello"))



