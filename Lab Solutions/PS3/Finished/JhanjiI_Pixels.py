# Ishaan Jhanji
# Pixels.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

line1 = "BBBBBBBBBB"
line2 = "BBNNBBNNBB"
line3 = "BBNNBBNNBB"
line4 = "BBBBBBBBBB"
line5 = "BBBBNNBBBB"
line6 = "BBNBBBBNBB"
line7 = "BBBNNNNBBB"
line8 = "BBBBBBBBBB"

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

numB = 0
numN = 0
total = 0
percent = 0.00

lines = [line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8]


numB = line1.count("B")
numB = numB + line2.count("B")
numB = numB + line3.count("B")
numB = numB + line4.count("B")
numB = numB + line5.count("B")
numB = numB + line6.count("B")
numB = numB + line7.count("B")
numB = numB + line8.count("B")

numN = line1.count("N")
numN = numN + line2.count("N")
numN = numN + line3.count("N")
numN = numN + line4.count("N")
numN = numN + line5.count("N")
numN = numN + line6.count("N")
numN = numN + line7.count("N")
numN = numN + line8.count("N")

total = numB + numN

percent = (float(numB)/float(total)) * 100

print str(percent) + " %"
