def get_profile_picture_dimension(twoD_list, LEN_PHOTO):
	for hw in twoD_list:
		if (int(hw[0]) < LEN_PHOTO or int(hw[1]) < LEN_PHOTO):
			print 'UPLOAD ANOTHER'
		elif (int(hw[0]) >= LEN_PHOTO and int(hw[1]) >= LEN_PHOTO):
			if (int(hw[0]) == int(hw[1])):
				print 'ACCEPTED'
			elif (int(hw[0]) == LEN_PHOTO and int(hw[1]) == LEN_PHOTO):
				print 'ACCEPTED'
			else:
				print 'CROP IT'
len_of_photo = raw_input()
photos = raw_input()
twoD_list = []
for photo in range(0, int(photos)):
	width_height = raw_input()
	twoD_list.append(width_height.split(' '))
get_profile_picture_dimension(twoD_list, int(len_of_photo))