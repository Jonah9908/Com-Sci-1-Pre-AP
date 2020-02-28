# Jonah Sims
# GoFish.py  

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
player1Hand = [2, 4, 6, 8, "J", "Q", "K"]
player2Hand = [3, 4, 9, 10, "A"] 
player1Guesses = [2, 8, "J", 4, "Q"]
player2Guesses = [6, 9, "A", 5, 3] 

'''

End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

def Fish(hand, guess):
    contains = False
    spot = 0
    while spot < len(hand):
        if hand[spot] == guess:
            contains = True
        spot += 1
    if contains:
        contains = "HERE'S MY CARD"
    else:
        contains = "GO FISH"
    return contains


spot = 0
for num in player1Guesses:
    print(Fish(player2Hand, player1Guesses[spot]))
    print(Fish(player1Hand, player2Guesses[spot]))
    spot += 1




    



