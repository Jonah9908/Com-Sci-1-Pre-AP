# Milan Patel
# Patel_Triangles.py

sides1 = [5, 6, 7, 8, 9]
sides2 = [5, 6, 8, 8, 10]
sides3 = [5, 5, 9, 8, 9]

import math


def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    a = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return a


def triangle_Type(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        triangleType = "equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangleType = "isosceles"
    else:
        triangleType = "scalene"
    return triangleType


spot = 0
for item in sides3:
    print(triangle_Type(sides1[spot], sides2[spot], sides3[spot]), "triangle with area %.2f" % area(sides1[spot], sides2[spot], sides3[spot]))
    spot += 1
