string = raw_input()
list =[0,0]
for i in string:
	if i == 'L':
		list[0] -= 1
	elif i == 'R':
		list[0] += 1
	elif i == 'D':
		list[1] -= 1
	elif i == 'U':
		list[1] += 1
print str(list[0]) + ' ' + str(list[1])