# Jonah Sims
# Lucky.py
# Done

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
    number = str(number)
    sum = 0
    spot = 0
    for num in number:
        sum += int(number[spot])
        spot += 1
    return sum

# Final call
spot = 0
output_num = 0
for len in numbers:
    output_num = sum_digets(numbers[spot])
    if output_num % 2 == 0:
        print("Lucky " + str(numbers[spot]))
    else:
        print("Not Lucky " + str(numbers[spot]))
    spot += 1

    

