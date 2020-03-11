# Milan Patel
# Lucky.py

numbers = [58264, 24864, 125689, 121212353545]


def sum_digits(number):
    num = str(number)
    spot = 0
    add = 0
    while spot < len(num):
        add += int(num[spot])
        spot += 1
    return add


spot_outer = 0
for items in numbers:
    number = numbers[spot_outer]
    counter = (sum_digits(numbers[spot_outer]))
    spot_outer += 1
    if counter % 2 == 0:
        print("Lucky", number)
    else:
        print("NOT Lucky", number)