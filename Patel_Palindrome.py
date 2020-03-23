# Milan Patel
# Palindrome.py


words = ["radar", "banana", "alababa", "Hannah", "racecar"]


def reverse(word):
    length = len(word)
    spot = length - 1
    new_word = ""
    while spot >= 0:
        letter = word[spot]
        new_word += letter.lower()
        spot -= 1
    return new_word


outer_spot = 0
for items in words:
    lowercase = words[outer_spot]
    word_check = reverse(words[outer_spot])
    if word_check == lowercase.lower():
        print("PALINDROME")
    else:
        print("just a word")
    outer_spot += 1
