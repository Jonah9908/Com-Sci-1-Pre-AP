# Jonah Sims
# Dvorak.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

qwerty = [' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
dvorak = [' ',"'",',', '.','p','y','f','g','c','r','l','a','o','e','u','i','d','t','n','s','-',';','q','j','k','x','b','m','w','v','z']

dvorakText = ",. jab dak. a ,rbe.pugs ycm. cb jrmlgy.p ojc.bj.v"

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

def converter(Ddorak1):
    spot = 0
    for num in dvorak:
        if Ddorak1 == dvorak[spot]: #todo does not work, needs fixing
            return spot # '==' function does not work, cannot find that its equal to anything
    spot += 1




print(converter('r'))

print(dvorak[30])

