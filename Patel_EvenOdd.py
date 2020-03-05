# Milan Patel
# Patel_EvenOdd
numbers = [11, 43, 52, 68, 110, 111, 120, 15, 4, 926]



def is_Even(number):
    if number % 2 == 0:
        even = True
    else:
        even = False
    return even


def is_Odd(number):
    if number % 2 != 0:
        odd = True
    else:
        odd = False
    return odd


spot = 0
evencount = 0

evenTotal = 0


def odd_total(odd):
    oddcount = 0
    oddTotal = 0
    spot = 0
    for items in odd:
        if is_Odd(odd[spot]):
            oddcount += 1
            oddTotal += odd[spot]
        spot += 1
    return oddTotal


def even_total(even):
    spot = 0
    evencount = 0
    evenTotal = 0
    for items in even:
        if is_Even(even[spot]):
            evencount += 1
            evenTotal += even[spot]
        spot += 1
    return evenTotal


etotal = even_total(numbers)
ototal = odd_total(numbers)

print("Even Total:", etotal)
print("Odd Total:", ototal)

if etotal > ototal:
    print("Even total is larger.")
elif etotal == ototal:
    print("The totals are the same.")
else:
    print("Odd Total is larger.")