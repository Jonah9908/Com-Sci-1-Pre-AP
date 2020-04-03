# First Last
# Recommendation.py
# Done

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

recLetter = "Sally is an exceptional student.  She is awesome.  She is brilliant.  She really knows how to program.  One of Sally's best traits is her ability to problem solve. When faced with a difficult problem, she analyzes the tasks at hand, and comes up with unique solution. Because of her character and hard work ethic, I would like to recommend Sally for everything she wants."

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

#Replaces everything

recLetter = recLetter.replace('Sally', 'Billy')
recLetter = recLetter.replace('She', 'He')
recLetter = recLetter.replace('she', 'he')
recLetter = recLetter.replace('her', 'his')

print(recLetter)



