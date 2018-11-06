n = input()
matrix = []
# matrix_bool = []
matrix = [[1, 0, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 0]]
matrix_bool_row = [False, False, False, False]
matrix_bool_col = [False, False, False, False]
print matrix
# for i in range(n):
#     matrix.append([])
#     matrix_bool.append([])
# for i in range(n):
#     for j in range(n):
#         num = input()
#         matrix[i].append(num)
#         matrix_bool[i].append(False)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix_bool_row[i] = True
            matrix_bool_col[j] = True

for i in range(len(matrix_bool_row)):
    if matrix_bool_row[i]:
        for j in range(len(matrix_bool_col)):
            matrix[i][j] = 0
for i in range(len(matrix_bool_col)):
    if matrix_bool_col[i]:
        for j in range(len(matrix_bool_row)):
            matrix[j][i] = 0
# print matrix_bool_row

print matrix
# print matrix_bool