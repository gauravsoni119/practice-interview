key, lock = map(int, raw_input().split(' '))
N = input()
list = map(int, raw_input().split(' '))

#new_key = key * list[0]
list.insert(0, key)
index = 0
count = 0
new_key = (list[0] * list[1]) % 100000
count += 1
if new_key == lock:
	print count
else:
	for i in range(1, len(list) - 1):
		if new_key == lock:
			break
		else:
			new_key = (new_key * list[i + 1])% 100000
			count += 1
	print count