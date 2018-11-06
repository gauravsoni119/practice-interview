from sys import stdin, stdout
n = input()
num = raw_input().split(' ')
q = input()
for i in range(0, q):
    a, b = stdin.readline().split(' ')
    xor_of_query = 0
    count = 0
    arr = num[int(a) - 1: int(b)]
    for j in range(len(arr)):
        if arr[j] == '0':
            count += 1
        xor_of_query = xor_of_query ^ int(arr[j])
    stdout.write('%s %s' % (xor_of_query, count) + '\n')

from sys import stdin
 
n = int(stdin.readline())
v = map(int, stdin.readline().split())
x = [i for i in v]
z = [0 for _ in xrange(n)]
for i in xrange(n):
    z[i] = not v[i]
for i in xrange(1, n):
    x[i] ^= x[i-1]
    z[i] += z[i-1]
q = int(stdin.readline())
for _ in xrange(q):
    l, r = map(int, stdin.readline().split())
    a, b = x[r-1], z[r-1]
    if l >= 2:
        a ^= x[l-2]
        b -= z[l-2]
    print '%d %d' % (a, b)