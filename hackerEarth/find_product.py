MODULO = 1000000007
def find_product(arr):
	arr = arr_elements.split(' ')
	product = 1
	for elem in arr:
		product = product * int(elem)
	return product % MODULO
arr_size = raw_input()
arr_elements = raw_input()
print find_product(arr_elements)