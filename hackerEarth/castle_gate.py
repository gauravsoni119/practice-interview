def get_xor_of_num(num):
	count = 0
	for num1 in range(1, num + 1):
		for num2 in range(1, num + 1):
			if num1 ^ num2 <= num and num1 != num2:
				count += 1
	return count / 2
test_cases = input()
for test_case in range(0, test_cases):
	num = input()
	print get_xor_of_num(num)