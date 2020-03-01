
#Calculates what grade corresponds with what point
def weighted_class(grade):
    if grade == 100:
        return 6
    elif grade == 99:
        return 5.9
    elif grade == 98:
        return 5.8
    elif grade == 97:
        return 5.7
    elif grade == 96:
        return 5.6
    elif grade == 95:
        return 5.5
    elif grade == 94:
        return 5.4
    elif grade == 93:
        return 5.3
    elif grade == 92:
        return 5.2
    elif grade == 91:
        return 5.1
    elif grade == 90:
        return 5.0
    elif grade == 89:
        return 4.9
    elif grade == 88:
        return 4.8
    elif grade == 87:
        return 4.7
    elif grade == 86:
        return 4.6
    elif grade == 85:
        return 4.5
    elif grade == 84:
        return 4.4
    elif grade == 83:
        return 4.3
    elif grade == 82:
        return 4.2
    elif grade == 81:
        return 4.1
    elif grade == 80:
        return 4.0
def unweighted_class(grade):
    if grade == 100:
        return 5
    elif grade == 99:
        return 4.9
    elif grade == 98:
        return 4.8
    elif grade == 97:
        return 4.7
    elif grade == 96:
        return 4.6
    elif grade == 95:
        return 4.5
    elif grade == 94:
        return 4.4
    elif grade == 93:
        return 4.3
    elif grade == 92:
        return 4.2
    elif grade == 91:
        return 4.1
    elif grade == 90:
        return 4.0
    elif grade == 89:
        return 3.9
    elif grade == 88:
        return 3.8
    elif grade == 87:
        return 3.7
    elif grade == 86:
        return 3.6
    elif grade == 85:
        return 3.5
    elif grade == 84:
        return 3.4
    elif grade == 83:
        return 3.3
    elif grade == 82:
        return 3.2
    elif grade == 81:
        return 3.1
    elif grade == 80:
        return 3.0

#Asks for Averages

HUG_Grade = float(input("HUG Grade::"))
PE_Grade = float(input("PE Grade::"))
MAPS_Grade = float(input("Prof_Comm Grade::"))
Geometry_Grade = float(input("Geometry Grade::"))
COM_SCI_Grade = float(input("Computer Science Grade::"))
English_Grade = float(input("English Grade::"))
Spanish_Grade = float(input("Spanish Grade::"))
Bio_Grade = float(input("Bio Grade::"))

#Converts Averages To GPA
HUG_Grade = weighted_class(HUG_Grade)
PE_Grade = unweighted_class(PE_Grade)
MAPS_Grade = unweighted_class(MAPS_Grade)
Geometry_Grade = weighted_class(Geometry_Grade)
COM_SCI_Grade = weighted_class(COM_SCI_Grade)
English_Grade = weighted_class(English_Grade)
Spanish_Grade = unweighted_class(Spanish_Grade)
Bio_Grade = weighted_class(Bio_Grade)


#Main Script to average.
average = 0
average = ((HUG_Grade + PE_Grade + MAPS_Grade + Geometry_Grade + COM_SCI_Grade + English_Grade + Spanish_Grade + Bio_Grade) / 8)

print("Your GPA is a ", average)


input("Press ENTER to stop program")



