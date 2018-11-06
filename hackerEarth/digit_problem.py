integer = raw_input().split()
num = list(integer[0])
k = int(integer[1])
new_str = ''
for i in range(len(num)):
	if num[i] != '9' and k !=0:
		new_str += '9'
		k -= 1
	else:
		new_str += num[i]
		
print new_str