test_cases = input()
for test_case in range(0, test_cases):
	n = input()
	arr = [0 for i in range(0,32)]
	bin_arr = []
	for i in range(0, n):
		num = input()
		bin_arr.append('{0:032b}'.format(num))
		#print bin_arr
	for i in range(len(arr) - 1, -1, -1):
		#print i
		for arr_bin in bin_arr:
			if arr_bin[i] == '1':
				arr[i] += 1
	#print arr
	print (len(arr) -1) - arr.index(max(arr))