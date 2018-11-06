def get_multiverse(arr_list):
	for arr in arr_list:
		print arr-1
total_arrays = int(raw_input(''))
arr_list = []
for arr in range(0, total_arrays):
	input_arr = raw_input('')
	arr_list.append(int(input_arr))
get_multiverse(arr_list)
	