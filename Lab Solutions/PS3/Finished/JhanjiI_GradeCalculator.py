# Ishaan Jhanji
# GradeCalculator.py

'''
Begin Required variables section:
=================================
Do not change the names of these variables at all.
You may change the values on the right side of the equals (=) sign if you
would like. For instance if you would like to have raw_input to be able to test
different user information, that's fine.
'''

grades=["D 100","D 50", "D 92","D 87","M 83","D 0","D 73","M 86"]

'''
End Required variables:
=======================
You may have any additional variables that you might need to complete
the program below this line.
'''

daily=[]
major=[]
spot = 0

while spot<len(grades):
    g=grades[spot]
    if g[:1]=="D":
        daily.append(int(g[1:5]))
    if g[:1]=="M":
        major.append(int(g[1:5]))
    spot+=1


a=daily.index(min(daily))
daily.insert(a, 100)
del daily[a+1]


a=daily.index(min(daily))
del daily[a]




avg_d=0
spot=0
while spot<len(daily):
    avg_d+=daily[spot]
    spot+=1
avg_d=avg_d/float(len(daily))
avg_d= float(avg_d * .4)

ma_avg=0
spot=0
while spot<len(major):
    ma_avg+=major[spot]
    spot+=1

ma_avg=ma_avg/float(len(major))
ma_avg=float(ma_avg * .6)

gr_avg=ma_avg+avg_d
gr_avg=round(gr_avg)
print "GRADE AVERAGE: %i"% (int(gr_avg))
