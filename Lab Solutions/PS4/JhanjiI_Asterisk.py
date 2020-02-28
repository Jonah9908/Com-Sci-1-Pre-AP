# Ishaan Jhanji
# Asterisk.py


import turtle

def asterisk():
    turtle.pendown()

    count = 0
    while count < 8:
       turtle.forward(100)
       turtle.back(100)
       turtle.right(45)
       count = count + 1
    turtle.penup()






asterisk()

turtle.done()
