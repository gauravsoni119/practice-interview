def get_subsequence_list(string):
	str = ''
	subsequence_list = []
	for char1 in range(0, len(string)):
		str += string[char1]
		for char2 in range(0, len(string)):
			str += string[char2]
		subsequence_list.append(str)
	return subsequence_list
		
test_cases = input()
for test_case in range(0, test_cases):
	s1 = raw_input()
	s2 = raw_input()
	s1 = get_subsequence_list(s1)
	s2 = get_subsequence_list(s2)
	print 'hackerearth' in s1
	print 'hackerearth' in s2