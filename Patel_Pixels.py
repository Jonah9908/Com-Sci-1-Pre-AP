# Milan Patel
# Pixels.py


line1 = "BBBBBBBBBB"
line2 = "BBNNBBNNBB"
line3 = "BBNNBBNNBB"
line4 = "BBBBBBBBBB"
line5 = "BBBBNNBBBB"
line6 = "BBNBBBBNBB"
line7 = "BBBNNNNBBB"
line8 = "BBBBBBBBBB"


def b_count(line):
    spot = 0
    count = 0
    for letters in line:
        if line[spot] == "B":
            count += 1
            spot += 1
        else:
            spot += 1
    return  count


total = b_count(line1) + b_count(line2) + b_count(line3) + b_count(line4) + b_count(line5) + b_count(line6) + b_count(
    line7) + b_count(line8)

combined = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8


percent = total / len(combined) * 100
number = "%.1f" % percent
print(number, "%")