# Jonah Sims
# PrimeCentury.py


def is_prime(integer):
    prime = True
    num = integer / 2
    spot = 2
    while num > spot:
        if integer % spot == 0:
            prime = False
        spot += 1
    return prime


count = 2000
for thing in range(2000, 2100):
    if is_prime(count):
        print(count)
    count += 1
