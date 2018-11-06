def get_reverse_of_string(input_str):
	new_str = ''
	for char in range(len(input_str),0, -1):
		new_str += input_str[char-1]
	return new_str
def is_palindromic_string(input_str):
	if get_reverse_of_string(input_str) == input_str:
		return 'YES'
	else:
		return 'NO'

input_str = raw_input()
print is_palindromic_string(input_str)
	