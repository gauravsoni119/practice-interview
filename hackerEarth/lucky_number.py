def is_has_two_set_bits(bin_num):
	count = 0
	for char in range(0, len(bin_num)):
		if bin_num[char] == '1':
			count += 1
	if count == 2:
		return True
	else:
		return False
def get_lucky_number(in_num):
	lucky_num_list = []
	count = 0
	while (in_num >= 0):
		bin_num = bin(count)
		if is_has_two_set_bits(bin_num):
			lucky_num_list.append(count)
		in_num -= 1
		count += 1
	return lucky_num_list
		
		
test_cases = input()
for test_case in range(0, test_cases):
	num = input()
	lucky_numbers = get_lucky_number(num)
	lucky_num_sum = 0
	for num in lucky_numbers:
		lucky_num_sum += num
	print lucky_num_sum % 1000000007