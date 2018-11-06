# Algo to find if string is permutation of other or not
def isPermutation(str1, str2):
	sortedStr1 = ''.join(sorted(str1))
	sortedStr2 = ''.join(sorted(str2))
	if(sortedStr1 == sortedStr2):
		return True
	else:
		return False

str1 = raw_input()
str2 = raw_input()
print isPermutation(str1, str2)