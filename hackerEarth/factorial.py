def factorial(num):
	fact = 1
	for num in range(1, int(input_num)+1):
		fact = num * fact
	return fact
input_num = raw_input()
print factorial(input_num)