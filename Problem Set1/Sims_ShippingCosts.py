# Jonah Sims
# ShippingCosts.py

area = 3
cost = 34.56
totalCost = 0

if area == 1 :
    totalCost = cost + (cost * .05)

if area == 2 :
    totalCost = cost + (cost * .12)


if area == 3 :
    totalCost = cost + (cost * .19)


if area == 4 :
    totalCost = cost + (cost * .29)

print("The cost to ship to Area " + str(area) + " is $%.2f"%totalCost)



    


