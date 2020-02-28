# Ishaan Jhanji
# TriangleSpiral.py

# Draws a series of triangles that draws a really cool pattern

import turtle

'''---------------------------------- Function Declaration ----------------------------------'''

def triangle(length):

    count = 0

    while count < 3:
        turtle.forward(length)
        turtle.right(120)
        count = count + 1

    turtle.right(5)

'''--------------------------------------- Code Logic ---------------------------------------'''


turtle.speed(.1)

turtle.pu()
turtle.goto(0,0)

sideLength = 10

turtle.pd()

while sideLength <= 400 :
    triangle(sideLength)
    sideLength = sideLength + 2


turtle.done()
