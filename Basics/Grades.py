








rawScores = [15, 86, 70, 38, 50]
spot = 0





while spot < len(rawScores):
    if rawScores[spot] >= 0 and rawScores[spot]<= 30:
        print("You got a 1")
    if rawScores[spot] >= 31 and rawScores[spot]<= 40:
        print("You got a 2")
    if rawScores[spot] >= 41 and rawScores[spot] <= 69:
        print("You got a 3")
    if rawScores[spot] >= 70 and rawScores[spot] <= 84:
        print("You got a 4")
    if rawScores[spot] >= 85:
        print("You got a 5")
    spot = spot + 1


        
    
    
