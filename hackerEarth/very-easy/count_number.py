test_cases = input()
for test_case in range(0, test_cases):
	N = input()
	S = raw_input()
	count = 0
	temp = 0
	for i in S:
		if i.isdigit():
			if temp == 0:
				temp += 1
			#print 'inside if', temp
		else:
			if temp != 0:
				count = count + temp
				temp = 0
			#print 'inside else', temp
	count  = temp + count
	print count