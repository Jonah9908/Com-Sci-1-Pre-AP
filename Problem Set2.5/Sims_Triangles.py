# Jonah Sims
# Triangles.py

sides1 = [5, 6, 7, 8, 9]
sides2 = [5, 6, 8, 8, 10]
sides3 = [5, 5, 9, 8, 9]

import math


# Calculates area
def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return a


# Determines what type of triangle it is
def triangle_type(side1, side2, side3):
    if side1 == side2 and side1 == side3 and side2 == side3:
        return "equilateral triangle"
    elif side1 != side2 and side1 != side3 and side2 != side3:
        return "scalene triangle"
    else:
        return "isosceles triangle"


# Final print statement / script
spot = 0
for len in sides1:
    print(triangle_type(sides1[spot], sides2[spot], sides3[spot]) + " with area " + "%.2f" % area(sides1[spot], sides2[spot], sides3[spot]))
    spot += 1
