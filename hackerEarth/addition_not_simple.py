alphabets = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13,
			'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
reverse_alphabets = {'24': 'x', '25': 'y', '26': 'z', '20': 't', '21': 'u', '22': 'v', '23': 'w', '1': 'a', '3': 'c', '2': 'b', '5': 'e',
			'4': 'd', '7': 'g', '6': 'f', '9': 'i', '8': 'h', '11': 'k', '10': 'j', '13': 'm', '12': 'l', '15': 'o', '14': 'n', '17': 'q',
			'16': 'p', '19': 's', '18': 'r'}

def get_addition_of_str(org_str, reverse_str):
	new_str = ''
	for i in range(len(org_str)):
		str_index = alphabets[org_str[i]] + alphabets[reverse_str[i]]
		if str_index > 26:
			new_str += reverse_alphabets[str(str_index-26)]
		else:
			new_str += reverse_alphabets[str(alphabets[org_str[i]] + alphabets[reverse_str[i]])]
	return new_str
test_cases = input()
for test_case in range(test_cases):
	org_str = raw_input()
	reverse_str = org_str[::-1]
	new_str = get_addition_of_str(org_str, reverse_str)
	print new_str