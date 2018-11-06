bin = raw_input()
count = 0
count1 = 0
for i in bin:
	if i == '0':
		count += 1
		if count1 < 6:
			count1 = 0
	elif i == '1':
		count1 += 1
		if count < 6:
			count = 0
if count >= 6 or count1 >= 6:
	print 'Sorry, sorry!'
else:
	print 'Good luck!'