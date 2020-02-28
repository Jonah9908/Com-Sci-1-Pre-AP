# Jonah Sims
# QualityControl.py

tests = [1,2,3,4,5,5,7,4,3]
spot = 0
test = 0
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0

while spot < len(tests):
    if tests[spot] == 1 :
        t1 = 1
    if tests[spot] == 2 :
        t2 = 1
    if tests[spot] == 3 :
        t3 = 1
    if tests[spot] == 4 :
        t4 = 1
    if tests[spot] == 5 :
        t5 = 1
    if tests[spot] == 6 :
        t6 = 1
    if tests[spot] == 7 :
        t7 = 1
    spot = spot + 1

test = int(t1) + int(t2) + int(t3) + int(t4) + int(t5) + int(t6) + int(t7)

if test == 7:
    print("Passed")
else: 
    print("Failed")
        
    

    

                                                    