from collections import Counter
N = int(input())
arr = raw_input().split()
Q = int(input())
c = Counter(arr)
for qr in xrange(Q):
    num = int(input())
    if num in c:
        print c[num]
    else:
        print 'NOT PRESENT'
