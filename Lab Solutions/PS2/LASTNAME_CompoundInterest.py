# Ishaan Jhanji
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

spot = 0
answer = 0
newRate = 0

while spot < len(rates):
    newRate = rates[spot] * 0.01
    answer = investments[spot] * ((newRate + 1) ** terms[spot])
    print "$%.2f"%(answer)
    spot = spot + 1
