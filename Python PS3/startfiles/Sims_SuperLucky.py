# First Last
# SuperLucky.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
nums = [1269, 1234, 1224, 2357, 527869, 555555, 4469]

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''


def is_prime(number):
    prime = True
    inum = number / 2
    count = 2
    while count <= inum:
        if number % count == 0:
            prime =  False
        count += 1
    if number == 1:
        prime =  False
    if number == 0:
        prime =  False
    return prime


for num in nums:

