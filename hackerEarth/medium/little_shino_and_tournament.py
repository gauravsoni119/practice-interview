#f = open('input1.txt')
#print f.readline().rstrip('\n').split(' ')
#print f.readline()
#print f.readline()
N, Q = map(int, raw_input().split(' '))
fighters = map(int, raw_input().split(' '))
#N, Q = map(int, f.readline().rstrip('\n').split(' '))
#fighters = map(int, f.readline().rstrip('\n').split(' '))
fighters_with_strength = {}
for i in range(0, len(fighters)):
	fighters_with_strength[i] = fighters[i]
#print fighters_with_strength,"***************"
fights = []
total_fights = []
query_list={}
for i in range(0, Q):
	fights.append(input())
#print fights
#for i in fighters:
#	total_fights.append(0)
for i in fights:
	query_list[i-1] = 0
#print query_list

#print total_fights, fights
#print N, Q, fights, fighters

#for i in range(0, len(fighters), 2):
#	fighters_pair.append(fighters[i:i+2])
while len(fighters_with_strength) != 1:
	winners = {}
	for i in range(0, len(fighters_with_strength), 2):
		if len(fighters_with_strength) % 2 == 0:
			pair = [fighters_with_strength[fighters_with_strength.keys()[i]], fighters_with_strength[fighters_with_strength.keys()[i + 1]]]
			winner = max(pair)
			if fighters_with_strength[fighters_with_strength.keys()[i]] == winner:
#				print fighters_with_strength.keys()[i],")))))))))))"
				winners[fighters_with_strength.keys()[i]] = winner
			else:
				winners[fighters_with_strength.keys()[i + 1]] = winner
#			print fighters_with_strength.keys()[i],"+++", fighters_with_strength.keys()[i+1]
			if fighters_with_strength.keys()[i] in query_list:
				query_list[fighters_with_strength.keys()[i]] += 1
			if fighters_with_strength.keys()[i + 1] in query_list:
				query_list[fighters_with_strength.keys()[i + 1]] += 1
		elif len(fighters_with_strength) % 2 != 0:
			if i != len(fighters_with_strength) - 1:
				pair = [fighters_with_strength[fighters_with_strength.keys()[i]], fighters_with_strength[fighters_with_strength.keys()[i + 1]]]
				winner = max(pair)
				if fighters_with_strength[fighters_with_strength.keys()[i]] == winner:
					winners[fighters_with_strength.keys()[i]] = winner
				else:
					winners[fighters_with_strength.keys()[i + 1]] = winner
#				print pair, winners,"****", i
				if fighters_with_strength.keys()[i] in query_list:
					query_list[fighters_with_strength.keys()[i]] += 1
				if fighters_with_strength.keys()[i + 1] in query_list:
					query_list[fighters_with_strength.keys()[i + 1]] += 1
#					print query_list,"^^^^^^^^",i+1
			else:
#				print 'inside else........', fighters_with_strength[fighters_with_strength.keys()[i]]
				#if fighters_with_strength.keys()[i] in query_list:
				#	query_list[fighters_with_strength.keys()[i]] += 1
				#winner_list.append(fighters_with_strength[i])
				winners[fighters_with_strength.keys()[i]] = fighters_with_strength[fighters_with_strength.keys()[i]]
#				print query_list,"-----------", winners
		#if len(fighters_pair[i]) == 2:
		#total_fights[fighters_pair[i][0] - 1] += 1
		#total_fights[fighters_pair[i][1] - 1] += 1
		else:
			pass
#			print fighters_pair[i],"=="
			#fights[fighters_pair[i][0] - 1] += 1
#		print ";;;;", winners
	fighters_with_strength = winners
#	print fighters_with_strength,"&&&"

#if query_list.get(i):
#	query_list[i] += 1
#if query_list.get(i + 1):
#	query_list[i + 1] += 1
#print query_list
for i in query_list:
	#print i, fights.index(i), "===", total_fights
	print query_list[i]