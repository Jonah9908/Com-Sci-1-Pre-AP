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
#Test

total = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10

large = 0
spot = 0
while spot < len(total) - 8 + 1:
    item = substring(total, spot, spot + 8)
    spot += 1
    if item == "oxoxxooo":
        large += 1



mcount = 0
spot = 0
while spot < len(total) - 3 + 1:
    item = substring(total, spot, spot + 3)
    spot += 1
    if item == "oxo":
        mcount += 1
medium = mcount - large

scount = 0
spot = 0
while spot < len(total) - 2 + 1:
    item = substring(total, spot, spot + 2)
    spot += 1
    if item == "oo":
        scount += 1
sub = 0
spot = 0
while spot < len(total) - 3 + 1:
    item = substring(total, spot, spot + 3)
    spot += 1
    if item == "ooo":
        sub += 1
Small = scount - sub * 2

print(Small, "small")
print(medium, "medium")
print(large, "large")
