def get_set_bits(bin_num):
	count = 0
	for char in str(bin_num):
		if char == '1':
			count += 1
	return count
test_cases = input()
for test_case in range(0, test_cases):
	input_num = input()
	bin_num = bin(input_num)
	print get_set_bits(bin_num)