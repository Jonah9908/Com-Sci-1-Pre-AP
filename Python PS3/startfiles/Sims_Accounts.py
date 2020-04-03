# First Last
# Accounts.py
# Done

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

deposits = ["0434512", "03145234", "012341347", "0511112345", "0475746", "03654534", "02112"]

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

club1 = 0
club2 = 0
club3 = 0
club4 = 0
club5 = 0

# Calculates total for each club
spot = 0
for num in deposits:
    num = deposits[spot]
    ID = num[0:2]
    amount = num[2::]
    amount = int(amount)
    if ID == "01":
        club1 += amount
    elif ID == "02":
        club2 += amount
    elif ID == "03":
        club3 += amount
    elif ID == "04":
        club4 += amount
    elif ID == "05":
        club5 += amount
    spot += 1

# Converts full number to number with cents

club1 = int(club1) / 100
club2 = int(club2) / 100
club3 = int(club3) / 100
club4 = int(club4) / 100
club5 = int(club5) / 100

# Print statements

print("1" , str(club1))
print("2" , str(club2))
print("3" , str(club3))
print("4" , str(club4))
print("5" , str(club5))


