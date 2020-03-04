# Jonah Sims
# EvenOdd.py

numbers = [11, 43, 52, 68, 110, 111, 120, 15, 4, 926]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def even_total(list1):
    spot = 0
    even_total = 0
    for num in list1:
        if is_even(list1[spot]):
            even_total += list1[spot]
        spot += 1
    return even_total





