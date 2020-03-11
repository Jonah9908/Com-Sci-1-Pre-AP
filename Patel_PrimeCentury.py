# Milan Patel
# PrimeCentury.py


def is_prime(year):
    prime = True
    num = year / 2
    count = 2
    while count < num:
        if year % count == 0:
            prime = False
        count += 1
    return prime


spot = 2000
for num in range(2000, 2100):
    if is_prime(spot):
        print(spot)
    spot += 1

