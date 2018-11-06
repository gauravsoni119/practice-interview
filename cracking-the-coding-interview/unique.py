# Algo to find string is unique or not
def isUniqueString(str):
	arr = ['' for i in range(128)]
	for i in range(0, len(str)):
		if str[i] in arr:
			return False
		arr[i] = str[i]
	return True

str = raw_input('')
print isUniqueString(str)