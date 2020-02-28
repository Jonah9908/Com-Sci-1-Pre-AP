# Ishaan Jhanji
# PrimeCentury.py


devide = 1
year = 2000
count = 0
mod = 0




while year < 2100:
    devide = 1
    count = 0
    while devide < (year + 1):
        mod = year % devide
        if mod == 0:
            count = count + 1
        devide = devide + 1
    if count == 2:
        print year
    year = year + 1
