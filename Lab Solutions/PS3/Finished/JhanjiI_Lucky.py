# Ishaan Jhanji
# Lucky.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

numbers = [58264, 24864, 125689, 121212353545]

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

number = ""
spot = 0
spotM = 0
total = 0

while spot < len(numbers):
    number = numbers[spot]
    number = str(number)
    spotM = 0
    total = 0
    while spotM < len(number):
        total = total + int(number[spotM])
        spotM = spotM + 1
    if (total % 2) == 0:
        print "Lucky " + str(number)
    else:
        print "NOT Lucky " + str(number)
    spot = spot + 1
