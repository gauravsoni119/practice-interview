def find_winner(N, K, X):
	if len(N) < X % K:
		del N[:]
		return X
	else:
		index = N.index(X)
		person = X % K
		if person > 0:
			for i in range(0, person):
				try:
					N.remove(N[index + 1])
				except Exception as e:
					N.remove(N[0])
					index = index - 1
		if(len(N) - 1 >= index + 1):
			return N[index + 1]
		else:
			return N[0] if len(N) > 0 else X

N, K, X = map(int, raw_input().split(' '))
N = [i for i in range(1, N + 1)]

while(len(N) != 1):
	X = find_winner(N, K, X)
	if len(N) == 0:
		break
if len(N) == 1:
	print  N[0]
else:
	print X