test_cases = input()
seven_segment_map = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
def get_seven_segment(num):
	seg_sum = 0
	for i in num:
		seg_sum = seg_sum + seven_segment_map[i]
	return seg_sum
for test_case in range(test_cases):
	len_of_fav_list = input()
	fav_list = raw_input().split()
	seven_segment_list = []
	for num in fav_list:
		seven_segment_list.append(get_seven_segment(num))
	fav_seg_index = seven_segment_list.index(min(seven_segment_list))
	print fav_list[fav_seg_index]