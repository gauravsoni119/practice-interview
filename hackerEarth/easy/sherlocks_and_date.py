MONTHS = ['January', 'February', 'March','April','May','June','July','August','September','October','November', 'December']
MONTHS_WITH_ODD_DAYS = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

def find_leap_year(year):
	if (year % 4) == 0:
		if (year % 100) != 0:
			return True
		elif (year % 400) == 0:
			return True
		else:
			return False
	else:
		return False


test_cases = input()
for test_case in range(0, test_cases):
	day, month, year = raw_input().split(' ')
	day = int(day)
	year = int(year)
	if day == 1 and month in MONTHS_WITH_ODD_DAYS:
		if MONTHS[MONTHS_WITH_ODD_DAYS.index(month)] == MONTHS[0]:
			print str(31) + ' ' + MONTHS[11] + ' ' + str(year - 1)
		elif MONTHS[MONTHS.index(month)] == MONTHS[7]:
			print str(31) + ' ' + MONTHS[MONTHS.index(month) - 1] + ' ' + str(year)
		elif day == 1 and MONTHS.index(month) == 2 and find_leap_year(year):
			print str(29) + ' ' + MONTHS[1] + ' ' + str(year)
		elif day == 1 and MONTHS.index(month) == 2 and not find_leap_year(year):
			print str(28) + ' ' + MONTHS[1] + ' ' + str(year)
		else:
			print str(30) + ' ' + MONTHS[MONTHS.index(month) - 1] + ' ' + str(year)
	elif day == 1 and month not in MONTHS_WITH_ODD_DAYS:
		print str(31) + ' ' + MONTHS[MONTHS.index(month) - 1] + ' ' + str(year)
	else:
		print str(day - 1) + ' ' + month + ' ' + str(year)