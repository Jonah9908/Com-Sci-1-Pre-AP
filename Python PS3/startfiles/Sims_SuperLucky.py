# Jonah Sims
# SuperLucky.py
# Done

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


def is_prime(integer):
    prime = True
    num = integer / 2
    spot = 2
    while num > spot:
        if integer % spot == 0:
            prime = False
        spot += 1
    if integer == 1:
        prime = False
    if integer == 4:
        prime = False
    return prime


spot = 0
for num in nums:
    big_num = str(nums[spot])
    num_spot = 0
    prime_count = 0
    while len(big_num) > num_spot:
        small_num = big_num[num_spot]
        small_num = int(small_num)
        if is_prime(small_num) is True:
            prime_count += 1
        num_spot += 1
    if prime_count == 0:
        print("not lucky")
    elif is_prime(prime_count):
        print("ULTIMATE")
    elif prime_count >= 1:
        print("SUPER")
    spot += 1


