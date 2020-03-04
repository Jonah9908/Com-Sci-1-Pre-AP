# Jonah Sims
# EvenOdd.py

numbers = [11, 43, 52, 68, 110, 111, 120, 15, 4, 926]


# checks to see if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# Adds up total even numbers
def even_total(list1):
    spot = 0
    even_total = 0
    for num in list1:
        if is_even(list1[spot]):
            even_total += list1[spot]
        spot += 1
    return even_total


# Adds up total odd  numbers
def odd_total(list1):
    spot = 0
    odd_total = 0
    for num in list1:
        if is_even(list1[spot]) == False:
            odd_total += list1[spot]
        spot += 1
    return odd_total


# Prints even total

print("Even total: " + str(even_total(numbers)))

# Prints odd total

print("Even total: " + str(odd_total(numbers)))

# Checks to see if even or odd total is higher

if even_total(numbers) > odd_total(numbers):
    print("Even total is larger.")
else:
    print("Odd total is larger.")
