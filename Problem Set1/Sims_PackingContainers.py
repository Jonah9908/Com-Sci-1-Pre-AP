# Jonah Sims
# PackingContainers.py
# In this program, the code will tell you how many numbers in the list can devide evenly into 20.



size = 20
itemSizes = range(1, 11)
spot = 0
count = 0


while spot < len(itemSizes):
    if size % itemSizes[spot] == 0:
        count = count + 1
    spot = spot + 1
    
    
print(str(count) + " of the items go evenly into " + str(size))




