from random import randrange
import time
rand = randrange(10)
question = input(str("What is your question? "))
reasponce = str("Idk")
print("In progress")


if rand == 0:
        reasponce = str("My sources say no")
elif rand == 1:
        reasponce = str("My sources say yes")
elif rand == 2:
        reasponce = str("My sources say maby")
elif rand == 3:
        reasponce = str("I cannot confirm nor deny")
elif rand == 4:
        reasponce = str("I cannot answer at this time")
elif rand == 5:
        reasponce = str("Most definitly")
elif rand == 6:
        reasponce = str("Most definitly not")
elif rand == 7:
        reasponce = str("100% Yes")
elif rand == 8:
        reasponce = str("100% No")
elif rand == 9:
        reasponce = str("There is a possibility")
else:
        reasponce = str("Dont get your hopes up")
    
    
time.sleep(4)
print(str(reasponce))








