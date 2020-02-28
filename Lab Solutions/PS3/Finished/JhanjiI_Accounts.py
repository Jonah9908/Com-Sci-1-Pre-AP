# Ishaan Jhanji
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

index = 0
dep = ""
length = 0
dep = deposits[index]
c_1=0
c_2=0
c_3=0
c_4=0
c_5=0


while index<len(deposits):
    dep=deposits[index]
    if "01" in dep:
        dep=dep[2:]
        length=len(dep)-2
        dep=dep[0:len(dep)-2]+"."+dep[length:len(dep)]
        c_1=float(c_1)+float(dep)
        c_1="%.2f"% c_1
    elif "02" in dep:
        dep=dep[2:]
        length=len(dep)-2
        dep=dep[0:len(dep)-2]+"."+dep[length:len(dep)]
        c_2=float(c_2)+float(dep)
        c_2="%.2f"% c_2
    if "03" in dep:
        dep=dep[2:]
        length=len(dep)-2
        dep=dep[0:len(dep)-2]+"."+dep[length:len(dep)]
        c_3=float(c_3)+float(dep)
        c_3="%.2f"% c_3
    elif "04" in dep:
        dep=dep[2:]
        length=len(dep)-2
        dep=dep[0:len(dep)-2]+"."+dep[length:len(dep)]
        c_4=float(c_4)+float(dep)
        c_4="%.2f"% c_4
    elif "05" in dep:
        dep=dep[2:]
        length=len(dep)-2
        dep=dep[0:len(dep)-2]+"."+dep[length:len(dep)]
        c_5=float(c_5)+float(dep)
        c_5="%.2f"% c_5
    index=index+1
print "1 "+ str(c_1)
print "2 "+ str(c_2)
print "3 "+ str(c_3)
print "4 "+ str(c_4)
print "5 "+ str(c_5)








'''
club1 = []
club2 = []
club3 = []
club4 = []
club5 = []

spot = 0
item = 0
itemCheck = 0

while spot < len(deposits):
    item = deposits[spot]
    itemCheck = item[0:2]
    print item[0:2]
    if itemCheck == 01:
        item = item[2::]
        item = item * 0.01
        club1.append(item)
    if itemCheck == 02:
        item = item[2::]
        item = item * 0.01
        club2.append("item")
    if itemCheck == 03:
        item = item[2::]
        item = item * 0.01
        club3.append(item)
    if itemCheck == 04:
        print "HI"
        item = item[2::]
        club4.append("item")
    if itemCheck == 05:
        item = item[2::]
        item = item * 0.01
        print item
    spot = spot + 1

print club4
'''
