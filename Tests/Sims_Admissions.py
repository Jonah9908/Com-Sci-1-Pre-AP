# Jonah Sims
# Admissions.py

# Do not change the variable name below

grades = [84, 81, 75, 96, 100, 85, 61, 92]

# Do not change the variable name above
# ----------------------------------------------------------------------------------------------------------------------

spot = 0
A = 0
B = 0
C = 0
D = 0
F = 0

# Converts number average to letter average
for num in grades:
    if grades[spot] >= 90:
        A += 1
    elif 90 > grades[spot] >= 80:
        B += 1
    elif 80 > grades[spot] >= 70:
        C += 1
    elif 70 > grades[spot] >= 60:
        D += 1
    elif 60 > grades[spot]:
        F += 1
    spot += 1


# Converts grade to 4.0 scale
def convert_grade(grade):
    if grade >= 90:
        return 4
    elif 90 > grade >= 80:
        return 3
    elif 80 > grade >= 70:
        return 2
    elif 70 > grade >= 60:
        return 1
    elif 60 > grades[spot]:
        return 0


# Average GPA
raw_GPA = 0
final_GPA = 0
spot = 0
for num in grades:
    raw_GPA += convert_grade(grades[spot])
    spot += 1
final_GPA ="%.2f" % (raw_GPA / len(grades))

# Determine if accepted
Decision = ""
if float(F) > 0 or float(final_GPA) < 3.2:
    Decision = "REJECT"
else:
    Decision = "Accept"

# Final print statement
print("A - " + str(A))
print("B - " + str(B))
print("C - " + str(C))
print("D - " + str(D))
print("F - " + str(F))
print("GPA : " + str(final_GPA))
print("Decision : " + Decision)
