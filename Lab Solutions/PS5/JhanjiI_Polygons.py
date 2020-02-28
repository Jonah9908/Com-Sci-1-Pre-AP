# Ishaan Jhanji
# Polygons.py

import turtle

def polygon(sides, length):

    count = 0

    turtle.fill(True)

    if sides % 2 == 0:

        turtle.color("blue")
    else:
        turtle.color("red")
    
    while count < sides:
        turtle.forward(length)
        turtle.right(360/sides)
        count = count + 1

    turtle.fill(False)


#------------------------------#
sides = 10

while sides > 3:
    polygon(sides, 50)
    sides = sides - 1

turtle.done()
