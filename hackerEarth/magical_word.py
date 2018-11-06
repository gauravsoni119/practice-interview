import sys
test_cases = input()
def get_prime_nums(num):
	num_obj = {}
	num_arr = []
	prime_num_arr = []
	for i in range(2, num + 1):
		num_obj[i] = True
		num_arr.append(i)

	for i in num_arr:
		for j in range(num_arr.index(i)+1, len(num_arr)):
			if num_arr[j] % i == 0:
				num_obj[num_arr[j]] = False

	for prime_num in num_obj:
		if num_obj[prime_num] == True:
			prime_num_arr.append(prime_num)
	return prime_num_arr

def get_ascii(char):
	return ord(char)

def get_nearest_to_prime(prime1, prime2, prime):
	nearest1 = prime - prime1
	nearest2 = prime2 - prime
	if nearest1 == nearest2:
		return prime1
	if nearest1 < nearest2:
		return prime1
	if nearest1 > nearest2:
		if prime2 in xrange(65, 91) or prime2 in xrange(97,123):
			return prime2
		else:
			return prime1
	else:
		return prime2
for test_case in range(0,test_cases):
	len_of_string = input()
	string = raw_input()
	magic_string = []
	for char in string:
		ascii_of_char = get_ascii(char)
		prime_nums = get_prime_nums(ascii_of_char)
		index_of_nearest_prime1 = prime_nums.index(prime_nums[len(prime_nums)-1])
		new_prime_nums = get_prime_nums(ascii_of_char*2)
		index_of_nearest_prime2 = new_prime_nums.index(new_prime_nums[index_of_nearest_prime1 + 1])
		magic_string.append(chr(get_nearest_to_prime(new_prime_nums[index_of_nearest_prime1], new_prime_nums[index_of_nearest_prime2], ascii_of_char)))
	sys.stdout.write(''.join(magic_string) + '\n')