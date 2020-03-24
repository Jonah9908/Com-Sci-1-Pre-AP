# Milan Patel
# Recommendation.py

recLetter = "Sally is an exceptional student.  She is awesome.  She is brilliant.  She really knows how to program.  " \
            "One of Sally's best traits is her ability to problem solve. When faced with a difficult problem, " \
            "she analyzes the tasks at hand, and comes up with unique solution. Because of her character and hard " \
            "work ethic, I would like to recommend Sally for everything she wants. "

insert = 0


def substring(sentence, start, end):
    word = ""
    spot = start
    while spot < end:
        word += sentence[spot]
        spot += 1
    return word


addedText = "Billy"
deletedText = "Sally"
spot = 0
while spot < len(recLetter) - 5 + 1:
    item = substring(recLetter, spot, spot + 5)
    spot += 1
    if item == "Sally":
        insert = spot - 1
        recLetter = recLetter[:insert] + addedText + recLetter[insert + len(deletedText):]

addedText = "his"
deletedText = "her"
spot = 0
while spot < len(recLetter) - 3 + 1:
    item = substring(recLetter, spot, spot + 3)
    spot += 1
    if item == "her":
        insert = spot - 1
        recLetter = recLetter[:insert] + addedText + recLetter[insert + len(deletedText):]

addedText = "he"
deletedText = "she"
spot = 0
while spot < len(recLetter) - 3 + 1:
    item = substring(recLetter, spot, spot + 3)
    spot += 1
    if item == "she":
        insert = spot - 1
        recLetter = recLetter[:insert] + addedText + recLetter[insert + len(deletedText):]

addedText = "He"
deletedText = "She"
spot = 0
while spot < len(recLetter) - 3 + 1:
    item = substring(recLetter, spot, spot + 3)
    spot += 1
    if item == "She":
        insert = spot - 1
        recLetter = recLetter[:insert] + addedText + recLetter[insert + len(deletedText):]

print(recLetter)
