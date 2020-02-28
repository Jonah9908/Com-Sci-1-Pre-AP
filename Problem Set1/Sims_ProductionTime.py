#Jonah Sims
# ProductionTime.py

numItems = int(input("How many items do you want to produce?"))
days = 0
hours = 0
minn = 0
time = 0
totalTime = 0
coolDown = 0

time = numItems * 127
coolDown = numItems // 143
coolDown = coolDown * 313

totalTime = time + coolDown

days = totalTime // 86400
totalTime = totalTime - (days * 86400)

hours = totalTime // 3600
totalTime =  totalTime - (hours * 3600)

minn = totalTime // 60
totalTime = totalTime - (minn * 60)



print ("%d days %02d:%02d:%02d"%(days, hours, minn, totalTime))



















