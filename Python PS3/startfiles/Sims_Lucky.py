# Jonah Sims
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

#Function to determine sum of digets and if its even
def sum_digets(number):
    sum = 0
    spot = 0
    for hello in number:
        sum += number[spot]
        spot += 1
    return sum


print(str(sum_digets(121212353545)))

