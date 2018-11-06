word = 'phackerekarthj'
a = ''
b = []
for i in range(0, 2**len(word)):
    for j in range(0, len(word)):
        if i & (1<<j):
            a += word[j]
    b.append(a)
    a = ''
print b
