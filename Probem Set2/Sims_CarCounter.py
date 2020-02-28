# Jonah Sims
# CarCounter.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
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

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''
def substring(sentence, start, end):
    word = ""
    spot = start
    while spot < end:
        word += sentence[spot]
        spot += 1
    return word


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

smallargecount = 0
spot = 0
while spot < len(total) - 2 + 1:
    item = substring(total, spot, spot + 2)
    spot += 1
    if item == "oo":
        smallargecount += 1
sub = 0
spot = 0
while spot < len(total) - 3 + 1:
    item = substring(total, spot, spot + 3)
    spot += 1
    if item == "ooo":
        sub += 1
Small = smallargecount - sub * 2

print(Small, "small")
print(medium, "medium")
print(large, "large")




