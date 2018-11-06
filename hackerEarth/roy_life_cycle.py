days = input()
l = []
l1 = []
max_streak = 0
for day in range(days):
	count = 0
	c = 0
	s = raw_input()
	for i in range(len(s)):
		if s[i] == 'C':
			count += 1
			try:
				if s[i] != s[i+1]:
					if day >= 1:
						if s[0] == 'C':
							l.append(max_streak+count)
							max_streak = 0
					if c < count:
						c = count
						l.append(count)
						l1.append(c)
						count = 0
					else:
						count = 0
			except Exception as e:
				max_streak = count
				count = 0
				pass
#print l1, l
print max(l1), max(l)