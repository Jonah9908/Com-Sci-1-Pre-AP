# Milan Patel
# PrimeCentury.py

def is_prime(year):
    prime = True
    num = year / 2
    count = 2
    while count < num:
        if year % count == 0:
            return "composite"
        count += 1
    return "prime"

print(is_prime(2003))