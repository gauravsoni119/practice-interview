n = input()
matrix = []
for i in range(n):
    matrix.append([])
for i in range(n):
    for j in range(n):
        num = input()
        matrix[i].append(num)
for layer in range(n/2):
    first = layer
    last = n -1 - layer
    for i in range(last):
        offset = i - first
        top = matrix[first][i]
        matrix[first][i] = matrix[last - offset][first]
        matrix[last - offset][first] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[i][last]
        matrix[i][last] = top
print matrix