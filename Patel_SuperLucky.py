# Milan Patel
# SuperLucky.py

nums = [1269, 1234, 1224, 2357, 527869, 555555, 4469]


def is_prime(number):
    prime = True
    num = number / 2
    count = 2
    while count <= num:
        if number % count == 0:
            prime = False
        count += 1
    if number == 1:
        prime = False
    if number == 0:
        prime = False
    return prime


outerspot = 0
while outerspot < len(nums):
    prime = 0
    spot = 0
    number = len(str(nums[outerspot]))
    while spot < number:
        num = nums[outerspot]
        nnn = str(num)
        n = nnn[spot]
        if is_prime(int(n)):
            prime += 1
        spot += 1
    if prime == 0:
        print("not lucky")
    elif is_prime(prime):
        print("ULTIMATE")
    elif prime > 0:
        print("SUPER")
    outerspot += 1
