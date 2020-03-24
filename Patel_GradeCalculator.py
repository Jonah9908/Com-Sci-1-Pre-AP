# Milan Patel
# GradeCalculator.py

grades = ["D 100", "D 50", "D 92", "D 87", "M 83", "D 0", "D 73", "M 86"]

daily = []
spot = 0
for items in grades:
    grade = grades[spot]
    number = grade[2::]
    if grade[0] == "D":
        daily.append(number)
    spot += 1

major = []
spot = 0
for items in grades:
    grade = grades[spot]
    number = grade[2::]
    if grade[0] == "M":
        major.append(number)
    spot += 1


def lowest_number(grade_type):
    in_spot = 0
    lowest = int(grade_type[0])
    while in_spot < len(grade_type):
        if int(grade_type[in_spot]) < int(lowest):
            lowest = grade_type[in_spot]
        in_spot += 1
    return int(lowest)


def lowest_spot(L):
    Lspot = 0
    item = 0
    lowest = int(L[0])
    while Lspot < len(L):
        if int(L[Lspot]) < int(lowest):
            lowest = L[Lspot]
            item = Lspot
        Lspot += 1
    return int(item)


low = lowest_number(daily)
low_spot = lowest_spot(daily)
daily.pop(low_spot)

low = lowest_number(daily)
low_spot = lowest_spot(daily)
daily.pop(low_spot)
daily.append("100")


def average(type):
    sum = 0
    Average_spot = 0
    while Average_spot < len(type):
        sum += int(type[Average_spot])
        Average_spot += 1
    type_average = sum / len(type)
    return type_average


major_weightedAverage = average(major) * .6
daily_weightedAverage = average(daily) * .4
gradeAverage = major_weightedAverage + daily_weightedAverage
print("GRADE AVERAGE:", "%.0f" % gradeAverage)
