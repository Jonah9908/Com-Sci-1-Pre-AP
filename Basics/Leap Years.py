#Jonah Sims
#Ifs Leap year lab
#This program will determine if a year is a leap year



#insert number after str
year = int(input("Year?"))


if year % 400 == 0 :
    print("///The year " + str(year) + " is a leap year")

elif year % 4 == 0:
    if not year % 100 == 0:
        print("//The year " + str(year) + " is a leap year")
else:
    print("/The year " + str(year) + " is a not leap year year")

















