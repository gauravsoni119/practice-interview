def find_next_same_year(year):
	odd_days = 0
	start_year_is_leap_year = find_leap_year(year)
	while(True):
		year += 1
		is_current_year_is_leap_year = find_leap_year(year)
		if is_current_year_is_leap_year:
			odd_days += 2
		else:
			odd_days += 1
		if odd_days % 7 == 0:
			if start_year_is_leap_year and is_current_year_is_leap_year:
				break
			elif not start_year_is_leap_year and not is_current_year_is_leap_year:
				break;
	return year

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

year = int(raw_input(''))
print find_next_same_year(year)
