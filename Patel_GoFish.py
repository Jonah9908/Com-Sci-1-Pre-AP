# Milan Patel
# Patel_GoFish.py  

player1Hand = [2, 4, 6, 8, "J", "Q", "K"]
player2Hand = [3, 4, 9, 10, "A"]
player1Guesses = [2, 8, "J", 4, "Q"]
player2Guesses = [6, 9, "A", 5, 3]


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
