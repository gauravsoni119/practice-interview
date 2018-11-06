def is_subset_and(z, s):
	new_s = s.split(' ')
	sub_list = []
	sub = ''
	for sub1 in new_s:
		sub += sub1
		for sub2 in new_s:
			sub =+ sub2 
	sub_list.append()
	print sub_list
	pass
test_cases = input()
for test_case in range(0, test_cases):
	z, n = raw_input().split(' ')
	s = raw_input()
	is_subset_and(z, s)
	print z, n