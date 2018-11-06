test_cases = input()
for test_case in range(0, test_cases):
	N, P = map(int, raw_input().split(' '))
	flag = ''
	a = map(int, raw_input().split(' '))
	for i in range(0, len(a)):
		for j in range(i+1, len(a)):
			#print i,j, '===', a[i] * a[j],'***', P
			if a[i] * a[j] == P:
				flag = 'Yes'
				break
			else:
				flag = 'No'
		if flag == 'Yes':
			break
	print flag