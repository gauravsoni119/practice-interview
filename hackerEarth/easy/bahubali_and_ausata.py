N, Q = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
for i in range(0, Q):
	L, R = map(int, raw_input().split(' '))
	code = 0
	code = sum(a[L-1:R])
	mean = code / (R - (L-1))
	print mean