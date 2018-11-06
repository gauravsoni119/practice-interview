TYPE_1 = 1
TYPE_2 = 2
N, Q = map(int, raw_input().split(' '))
A = map(int, raw_input().split(' '))
for query in range(0, Q):
	type, index, num = map(int, raw_input().split(' '))
	sum_range = 0
	if type == TYPE_1:
		A[index] = num
	else:
		arr_range =  num + 1
#		print len(A), arr_range
		if arr_range <= len(A):
			for i in range(index, arr_range):
				sum_range += A[i]
			print sum_range, '\n'
		else:
			print -1
	sum_range = 0
				