import datetime

t = datetime.time(4, 55, 1)
print t
print 'Hours{%s}-Minutes{%s}-Seconds{%s}'%(t.hour, t.minute, t.second)

d = datetime.date.today()
print d.day

d1 = datetime.date(2018, 02,20)
d2 = datetime.date(2017, 02, 20)

print 'Y{%s} M{%s} D{%s}'%(d1.year, d1.month, d1.day)

print 'Difference between d1(date) and d2(date) - ', d1 - d2