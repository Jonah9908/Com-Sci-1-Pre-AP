# Ishaan Jhanji
# Pyramid.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

levels = 15

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''
import turtle

def rectangle(x,y):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(25)
    turtle.penup()


x = 0
y = 20 * levels

n = 0
for g in range(levels):
    turtle.penup()
    if n==1:
        rectangle(x,y)
        x = 0-(25*n)
        y = y-20
        n=n+1
    else:
        for j in range(n):
            rectangle(x,y)
            x = x+50
            turtle.penup()
        x = 0-(25*n)
        y = y-20
        n=n+ 1

turtle.done()
