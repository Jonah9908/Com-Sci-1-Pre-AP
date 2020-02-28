# Ishaan Jhanji
# Target.py


import turtle

def target():
    turtle.speed(.3)
    r = 100
    i = 0
    while i < 5:
        if i % 2 ==0:
            turtle.color("red")
            turtle.fill(True)
            turtle.circle(r)
            turtle.penup()
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.pendown()
            turtle.fill(False)
        else:
            turtle.color("white")
            turtle.fill(True)
            turtle.circle(r)
            turtle.penup()
            turtle.left(90)
            turtle.forward(20)
            turtle.right(90)
            turtle.pendown()
            turtle.fill(False)

        i = i + 1
        r = r-20

target()
turtle.done()
