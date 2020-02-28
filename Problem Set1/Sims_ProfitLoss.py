# Jonah Sims
# ProfitLoss.py

sales = [5, 1, 3, 2, 4]	
cost = 300.25
net = 0
loss = 0
spot = 0

while spot < len(sales):
     net = sales[spot] * 18.5 + net
     spot = spot + 1

loss = net - cost

print("your net total is $" + str(loss))











