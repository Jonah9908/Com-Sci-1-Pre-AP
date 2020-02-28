# Jonah Sims
# Geometry.py 

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''
radiusList = [1, 10,  123.456]
'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''
import math
PI = math.pi


#Function to calculatr surface area

def surface_area(radius1):
    SA = (4 * PI) * (radius1 * radius1)
    return(SA)

#Function to calculate volume

def volume(radius2):
    volume = (4/3) * (PI) * (radius2 ** 3)
    return(volume)

#Main Script

spot = 0

for len in radiusList:
    print( "SA = {0:.3f}".format(surface_area(radiusList[spot])), "V = {0:.3f}".format(volume(radiusList[spot])))
    spot = spot + 1







    
    



