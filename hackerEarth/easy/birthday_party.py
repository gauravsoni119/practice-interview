test_cases = input()
for test_case in range(0, test_cases):

	N, M = map(int, raw_input().split(' '))
	if M % N == 0:
		print 'Yes'
	else:
		print 'No'