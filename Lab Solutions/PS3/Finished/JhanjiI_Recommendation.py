# Ishaan Jhanji
# Recommendation.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

recLetter = "Sally is an exceptional student.  She is awesome.  She is brilliant.  She really knows how to program.  One of Sally’s best traits is her ability to problem solve. When faced with a difficult problem, she analyzes the tasks at hand, and comes up with unique solution. Because of her character and hard work ethic, I would like to recommend Sally for everything she wants."

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

numS = recLetter.count("Sally")
numSh = recLetter.count("She")
count = 0

delete_text = "She"
insert_text = "He"

while count < numSh:
    delete_text = "She"
    insert_test = "He"
    while delete_text in recLetter:
        index_delete_text = recLetter.index(delete_text)
        recLetter = recLetter[0:index_delete_text] + insert_text + recLetter[index_delete_text + len(delete_text):len(recLetter)]
    count = count + 1


delete_text = "Sally"
insert_text = "Billy"
count = 0

while count < numS:
    delete_text = "Sally"
    insert_test = "Billy"
    while delete_text in recLetter:
        index_delete_text = recLetter.index(delete_text)
        recLetter = recLetter[0:index_delete_text] + insert_text + recLetter[index_delete_text + len(delete_text):len(recLetter)]
    count = count + 1

print recLetter
