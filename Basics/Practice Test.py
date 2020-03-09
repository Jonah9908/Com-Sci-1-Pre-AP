grades = [90, 95, 100, 88, 76, 76, 94, 100]




F = []




#Checks grades for F

spot = 0
for num in grades:
    if 60 >= grades[spot]: #IDK the failing grade so im putting it as 60
         F.append(grades[spot])
    spot += 1

#calculates GPA
GPA = 0
spot = 0
for num in grades:
    if grades[spot] >= 90:
        GPA += 4
    elif 90 < grades[spot] >= 80:
        GPA += 3
    elif 80 < grades[spot] >= 70:
        GPA += 2
    elif 70 < grades[spot] >= 60:
        GPA += 1
    spot += 1


GPA = GPA / spot

#determines who is accepted


if len(F) > 0 or GPA >= 3.2:
    print("You were not accepted")
else:
    print("You are accepted")

        


