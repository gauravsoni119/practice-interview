test_cases = input()
def determine_winner(bob_soldier, alice_soldier):
	if bob_soldier > alice_soldier:
		return 'Bob'
	elif bob_soldier < alice_soldier:
		return 'Alice'
for test_case in range(test_cases):
	total_soldiers = input()
	bob_army = raw_input().split()
	bob_army = [int(soldier) for soldier in bob_army]
	alice_army = raw_input().split()
	alice_army = [int(soldier) for soldier in alice_army]
	max_strength_soldier_of_bob_army = max(bob_army)
	max_strength_soldier_of_alice_army = max(alice_army)
	if max_strength_soldier_of_bob_army == max_strength_soldier_of_alice_army:
		print 'Tie'
	elif max_strength_soldier_of_bob_army > max_strength_soldier_of_alice_army:
		print 'Bob'
	elif max_strength_soldier_of_bob_army < max_strength_soldier_of_alice_army:
		print 'Alice'
	#bob_win_count = 0
	#alice_win_count = 0
	'''for i in range(total_soldiers):
		winner = determine_winner(int(bob_army[i]), int(alice_army[i]))
		if winner == 'Bob':
			bob_win_count += 1
		elif winner == 'Alice':
			alice_win_count += 1
	if bob_win_count == alice_win_count:
		print 'Tie'
	elif bob_win_count > alice_win_count:
		print 'Bob'
	elif alice_win_count > bob_win_count:
		print 'Alice'''