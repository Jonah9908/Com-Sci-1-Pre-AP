# Ishaan Jhanji
# Checkerboard.py

import turtle

turtle.speed(.5)


def blackSquare():
    turtle.color("black")
    turtle.fill(True)
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.fill(False)
    turtle.forward(20)

def redSquare():
    turtle.color("red")
    turtle.fill(True)
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.fill(False)
    turtle.forward(20)

#--------------------------------------------------#
    
i = 0
y = -20

while i < 8:
    if i % 2 == 0:
        for f in range(4):
            blackSquare()
            redSquare()
    if i % 2 == 1:
        for f in range(4):
            redSquare()
            blackSquare()
    turtle.penup()
    turtle.goto(0,y)
    y = y - 20
    i = i + 1
    turtle.pendown()

turtle.done()
