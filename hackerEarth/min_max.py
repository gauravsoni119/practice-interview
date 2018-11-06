size = input()
array = raw_input().split()
array = [int(i) for i in array]
max = int(max(array))
min = int(min(array))
lis = []
count = 0
for i in range(min, max):
	lis.append(i)
for j in range(len(lis)):
	if lis[j] in array:
		count += 1
if count == len(lis):
	print 'YES'
else:
	print 'NO'