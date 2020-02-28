# Milan Patel
# Patel_CarCounter.py

line1 = "xooxxxxooxxxxoxoxxxxoxoxxxxxxxoxoxxoooxxxxxxxxxxxx"
line2 = "ooxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
line3 = "oxoxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
line4 = "oxoxxoooxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
line5 = "xxxoxoxxoooxxxxxxoxoxxoooxxxxxxxxoxoxxoooxxxxxxxxx"
line6 = "xoxoxxoooxxxxxooxxxooxxooxxooxxxxxooxxxxooxxxxooxx"
line7 = "oxoxxoxoxxoxoxxoxoxxoxoxxxxxxxoxoxxxxxoxoxxxxxoxox"
line8 = "xooxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoo"
line9 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
line10 = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxoxoxxooo"


def substring(sentence, start, end):
    word = ""
    spot = start
    while spot < end:
        word += sentence[spot]
        spot += 1
    return word


total = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10


def largecount(line):
    large = 0
    spot = 0
    while spot < len(line) - 8 + 1:
        item = substring(line, spot, spot + 8)
        spot += 1
        if item == "oxoxxooo":
            large += 1
    return large


largeTotal = 0
largeTotal += largecount(line1)
largeTotal += largecount(line2)
largeTotal += largecount(line3)
largeTotal += largecount(line4)
largeTotal += largecount(line5)
largeTotal += largecount(line6)
largeTotal += largecount(line7)
largeTotal += largecount(line8)
largeTotal += largecount(line9)
largeTotal += largecount(line10)


def mediumcount(line):
    medium = 0
    spot = 0
    while spot < len(line) - 3 + 1:
        item = substring(line, spot, spot + 3)
        spot += 1
        if item == "oxo":
            medium += 1
    return medium


mediumTotal = 0
mediumTotal += mediumcount(line1)
mediumTotal += mediumcount(line2)
mediumTotal += mediumcount(line3)
mediumTotal += mediumcount(line4)
mediumTotal += mediumcount(line5)
mediumTotal += mediumcount(line6)
mediumTotal += mediumcount(line7)
mediumTotal += mediumcount(line8)
mediumTotal += mediumcount(line9)
mediumTotal += mediumcount(line10)
mediumTotal -= largeTotal


def smallcount(line):
    small = 0
    spot = 0
    while spot < len(line) - 2 + 1:
        item = substring(line, spot, spot + 2)
        spot += 1
        if item == "oo":
            small += 1
    return small


smallTotal = 0
smallTotal += smallcount(line1)
smallTotal += smallcount(line2)
smallTotal += smallcount(line3)
smallTotal += smallcount(line4)
smallTotal += smallcount(line5)
smallTotal += smallcount(line6)
smallTotal += smallcount(line7)
smallTotal += smallcount(line8)
smallTotal += smallcount(line9)
smallTotal += smallcount(line10)
smallTotal -= 2 * largeTotal

print(smallTotal, "small")
print(mediumTotal, "medium")
print(largeTotal, "large")
