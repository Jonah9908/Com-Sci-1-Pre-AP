# Ishaan Jhanji
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

spot = 0
num = 2
spotQ = 0
numQ = 2
prime = 0

while spot < len(nums):
    spotQ = 0
    while spotQ < len(str(nums[spot])):
        number = str(nums[spot])
        if int(number[spotQ]) == 1:
            spotQ = spotQ + 1
        elif int(number[spotQ]) == num:
            prime = prime + 1
            spotQ = spotQ + 1
            num = 2
        elif int(number[spotQ]) % num ==0:
            spotQ = spotQ + 1
            num = 2
        else:
            num = num + 1
    if prime >= 1:
        spotQ = 0
        while spotQ < 1:
            if prime  == 1:
                print "SUPER"
                spotQ = spotQ + 1
            elif prime == numQ:
                print "ULTIMATE"
                spotQ = spotQ + 1
            elif prime % numQ == 0 :
                print "SUPER"
                spotQ = spotQ + 1
            else:
                numQ = numQ + 1
    else :
        print "not lucky"
    spot = spot + 1
    prime = 0
