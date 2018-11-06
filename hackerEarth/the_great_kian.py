num = input()
int_list = raw_input()
seq = int_list.split(' ')
lis = [0,0,0]
for i in range(3):
	if i < num:
		lis[i] = int(lis[i]) + int(seq[i])
		for j in range(i+3, num, 3):
			lis[i] = lis[i] + int(seq[j])
	else:
		break
print "%d %d %d"%(lis[0],lis[1],lis[2])