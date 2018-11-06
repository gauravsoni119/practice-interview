test_cases = input()
x,y = (1,1)
for test_case in range(test_cases):
	m,n = raw_input().split()
	(m,n) = (int(m), int(n))
	cards = input()
	for card in range(cards):
		a,b = raw_input().split()
		(a,b) = (int(a), int(b))
		#print m,n
		while a < m:
			a = a + 1
		#	print a
		while b < n:
			b = b + 1
		#	print b
		#print '(a,b)',(a,b)
		temp1 = x
		temp2 = y
		x,y = x + (a - 1), y + (b - 1)
		if (x,y) > (m,n):
			x,y = temp1, temp2
	print x
	