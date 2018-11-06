def find_fredo_consequence(ammo, obstacles, obstacle_list):
	obstacle_index = -1
	for i in range(0, len(obstacle_list)):
		if obstacle_list[i] == 0:
			ammo -= 1
		elif obstacle_list[i] == 1:
			ammo += 2
		if ammo <= 0 and i != len(obstacle_list) - 1:
			obstacle_index = i + 1
			break
	return 'No {}'.format(obstacle_index) if obstacle_index > -1 else 'Yes {}'.format(ammo)
			

test_cases = input()
for test_case in range(0, test_cases):
	ammo, obstacles = map(int, raw_input().split())
	obstacle_list = map(int, raw_input().split())
	print find_fredo_consequence(ammo, obstacles, obstacle_list)