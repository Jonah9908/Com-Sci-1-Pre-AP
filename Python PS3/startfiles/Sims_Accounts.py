# First Last
# Accounts.py

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

club1 = []
club2 = []
club3 = []
club4 = []
club5 = []

# Identifies which club the deposit is going too
def club_identifier(ID):
    if ID[0:2] == "01":
        club1.append(ID[2:])
    elif ID[0:2] == "02":
        club2.append(ID[2:])
    elif ID[0:2] == "03":
        club3.append(ID[2:])
    elif ID[0:2] == "04":
        club4.append(ID[2:])
    elif ID[0:2] == "05":
        club5.append(ID[2:])

#Function to calculate the total amount for every club
spot = 0
def club_total(club):
    total = 0
    for num in club:
             spot += 1

    return spot #getting an error on returning spot, I have no clue

print(club_total(club3))




'''
first = ((club1[0])[-2])
last =  ((club1[0])[-2])
'''

