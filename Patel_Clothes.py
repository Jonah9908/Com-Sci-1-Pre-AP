# Milan Patel
# Patel_Clothes.py  


clothes = ["P khaki", "S blueish green", "S apple", "K bright", "P blue", "P red", "K purple", "S ugly", "K stupid",
           "P big red"]
spot = 0
pants = []
shirts = []
socks = []
length = (len(clothes) - 1) - spot
item = clothes[length]


def substring(sentence, start, end):
    word = ""
    spot = start
    while spot < end:
        word += sentence[spot]
        spot += 1
    return word


for item in clothes:
    description = substring(item, 2, len(item))
    if item[0] == "S":
        shirts.append(description)
    elif item[0] == "P":
        pants.append(description)
    elif item[0] == "K":
        socks.append(description)
    spot += 1

L = len(shirts)

if len(pants) < L:
    L = len(pants)

if len(socks) < L:
    L = len(socks)

spot = 0
while spot < L:
    print(shirts[len(shirts) - spot - 1] + ", " + pants[len(pants) - spot - 1] + ", " + socks[len(socks) - spot - 1])
    spot += 1
