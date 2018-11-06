def count_one_in_binary(n):
	count = 0
	while(n):
		n = n & n-1
		count += 1
	return count
		
test_cases = input()
for test_case in range(0, test_cases):
	N = input()
	num_of_ones_in_N = count_one_in_binary(N)
	num = N + 1
	while True:
		is_num_greater = count_one_in_binary(num)
		if is_num_greater - num_of_ones_in_N == 1:
			print num
			break
		else:
			num = num + 1