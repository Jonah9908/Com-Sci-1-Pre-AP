# Ishaan Jhanji
# Clothes.py  

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

clothes = ["P khaki", "S blueish green", "S apple", "K bright",  "P blue", "P red", "K purple",  "S ugly", "K stupid", "P big red"] 

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

pants = []
shirts = []
socks = []
item = ""
itemType = ""
spot= 0
length = 0

while spot < len(clothes):
    item = clothes[spot]
    itemType = item[0]
    item = item[2::]
    if itemType == "P":
        pants.insert(0, item)
    if itemType == "S":
        shirts.insert(0, item)
    if itemType == "K":
        socks.insert(0, item)
    spot = spot + 1

length = len(shirts)

if len(pants) < length:
    length = pants
if len(socks) < length:
    length = socks

spot = 0

while spot < length:
    print shirts[spot] + ", " + pants[spot] + ", " + socks[spot]
    spot = spot + 1


