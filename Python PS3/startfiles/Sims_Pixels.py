# Jonah Sims
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

# Calculates number of black pixles
image = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8
spot = 0
count = 0
for num in image:
    if image[spot] == "B":
        count += 1
    spot += 1


#Calculates percentage

Percentage = (count / len(image)) * 100


print("%.1f" % Percentage + "%" )
