# Milan Patel
# Accounts.py

deposits = ["0434512", "03145234", "012341347", "0511112345", "0475746", "03654534", "02112"]


club1 = 0
club2 = 0
club3 = 0
club4 = 0
club5 = 0
for item in deposits:
    length = len(str(item))
    amount1 = item[2:length]
    if item[1] == "1":
        club1 += int(amount1)
    elif item[1] == "2":
        club2 += int(amount1)
    elif item[1] == "3":
        club3 += int(amount1)
    elif item[1] == "4":
        club4 += int(amount1)
    elif item[1] == "5":
        club5 += int(amount1)

deposit1 = club1 / 100
deposit2 = club2 / 100
deposit3 = club3 / 100
deposit4 = club4 / 100
deposit5 = club5 / 100
print("1", deposit1)
print("2", deposit2)
print("3", deposit3)
print("4", deposit4)
print("5", deposit5)
