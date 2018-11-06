test_cases = input()
for test_case in range(test_cases):
	count = 0
	command = raw_input()
	if 'B' in command:
		wall_list = command.split('B')
		for i in range(len(wall_list)):
			if i == 0:
				if len(wall_list[i]) >= 2:
					count += 2
				elif len(wall_list[i]) == 1:
					count += 1
			elif i == len(wall_list) - 1:
				if command.endswith('B'):
					if len(wall_list[i]) >= 4:
						count += 4
					elif len(wall_list[i]) == 3:
						count += 3
					elif len(wall_list[i]) ==2:
						count += 2
					elif len(wall_list[i]) ==1:
						count += 1
				else:
					if len(wall_list[i]) >= 2:
						count += 2
					elif len(wall_list[i]) == 1:
						count += 1
			else:
				if len(wall_list[i]) >= 4:
					count += 4
				elif len(wall_list[i]) == 3:
						count += 3
				elif len(wall_list[i]) ==2:
					count += 2
				elif len(wall_list[i]) ==1:
					count += 1
		print count
	else:
		print count