# Milan Patel
# Patel_EasyCode.py  

sentence = ["this", "is", "a", "test", "of", "the", "emergency", "broadcast", "system"]
def code(word):
    spot = 0
    term = ""
    while(spot < len(word)):
        term = term + word[spot]
        spot += 2
    spot = 1
    while(spot < len(word)):
        term = term + word[spot]
        spot += 2
    return term

Fcode = ""
sentencespot = 0
for word in sentence:
    Fcode += code(sentence[sentencespot]) + " "
    sentencespot += 1

Fcode = Fcode[0:len(Fcode) - 1] + "."
print(Fcode.capitalize())
