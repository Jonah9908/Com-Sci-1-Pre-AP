# Jonah Sims
# Palindrome.py
# Done

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
#Checks to see if word is a palindrome
def reverse(word):
    spot = len(word) - 1
    new_word = ""
    while spot >= 0:
        new_letter = word[spot]
        new_word = new_word + new_letter
        spot -= 1
    return new_word

#Loop that runs it it through the list
spot = 0
for num in words:
    original_word = words[spot]
    original_word =  original_word.lower()
    reverse_word = reverse(original_word)
    if original_word == reverse_word:
        print("PALINDROME")
    else:
        print("just a word")
    spot += 1





