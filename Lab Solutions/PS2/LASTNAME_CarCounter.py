# First Last
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

data = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10


total = 0
spot = 0
smallTotal = 0
medTotal = 0
largeTotal = 0

smallTotal = smallTotal + data.count("xoox")
medTotal = medTotal + data.count("oxo")
largeTotal = largeTotal + data.count("oxoxxooo")



print str(smallTotal) + " small"
print str((medTotal - largeTotal)) + " medium"
print str(largeTotal) + " large"
