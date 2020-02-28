# Jonah Sims
# CompoundInterest.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
investments = [10000.00, 10000.00, 10000.00, 10000.00, 1.00]
rates = [5.0, 5.0, 10.0, 10.0, 50.00]
terms = [20, 40, 20, 40, 40]
'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''


#Calculates the total intrest
def total_payment(investments,rates,terms):    
    rate = rates * .01
    intrest = (((1 + rate) ** terms) * investments)
    return intrest


#main script

spot = 0

for num in investments:
    print( "${0:.2f}".format(total_payment(investments[spot],rates[spot],terms[spot])))
    spot = spot + 1










