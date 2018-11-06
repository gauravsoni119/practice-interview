from collections import Counter

l = [1,2,3,34,5,5,6,7,7]

c = Counter(l)
print c

s = 'Hello World! The common text to become awesome programmer in World!'

c1 = Counter(s.split(' '))
print c1
print c1.most_common()
print list(c1)