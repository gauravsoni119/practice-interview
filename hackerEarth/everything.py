import copy
BREAK_LOOP_NUM = 42
num_arr = []
while True:
	num = input()
	if num != BREAK_LOOP_NUM:
		print num
	else:
		break
#print num_arr
#for num in range(1, len(num_arr)):
#	print num
#	if num_arr[num] < num_arr[num-1]:
#		elem = copy.copy(num_arr[num])
#		num_arr[num] = num_arr[num-1]
#		num_arr[num-1] = elem
#print num_arr