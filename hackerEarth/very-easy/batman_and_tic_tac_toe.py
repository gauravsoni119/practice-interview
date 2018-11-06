def is_batman_wins(positions):
    for i in range(len(positions)):
        for j in range(len(positions[i])):
            if j > 0 and j < 3:
                if positions[i][j] == 'x' and positions[i][j - 1] == 'x' and positions[i][j + 1] == '.':
                    return 'YES'
                elif positions[i][j] == '.' and positions[i][j - 1] == 'x' and positions[i][j + 1] == 'x':
                    return 'YES'
                elif positions[i][j] == 'x' and positions[i][j - 1] == '.' and positions[i][j + 1] == 'x':
                    return 'YES'
                elif j == 1 and i == 0:
                    if positions[i][j] == 'x' and positions[i + 1][j + 1] == 'x' and positions[i + 2][j + 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j + 1] == 'x' and positions[i + 2][j + 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j + 1] == '.' and positions[i + 2][j + 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
                elif j == 2 and i == 3:
                    if positions[i][j] == 'x' and positions[i - 1][j - 1] == 'x' and positions[i - 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i - 1][j - 1] == 'x' and positions[i - 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i - 1][j - 1] == '.' and positions[i - 2][j - 2] == 'x':
                        return 'YES'
                elif j == 2 and i == 0:
                    if positions[i][j] == 'x' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j - 1] == '.' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
                elif j == 2 and i == 1:
                    if positions[i][j] == 'x' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j - 1] == '.' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
                elif j ==1 and i == 1:
                    if positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
            elif j == 0:
                if positions[i][j] == 'x' and positions[i][j + 1] == 'x' and positions[i][j + 2] == '.':
                    return 'YES'
                elif positions[i][j] == '.' and positions[i][j + 1] == 'x' and positions[i][j + 2] == 'x':
                    return 'YES'
                elif positions[i][j] == 'x' and positions[i][j + 1] == '.' and positions[i][j + 2] == 'x':
                    return 'YES'
                elif i == 0:
                    if positions[i][j] == 'x' and positions[i + 1][j + 1] == 'x' and positions[i + 2][j + 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j + 1] == 'x' and positions[i + 2][j + 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j + 1] == '.' and positions[i + 2][j + 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
                elif i == 1:
                    if positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
            elif j == 3:
                if positions[i][j] == 'x' and positions[i][j - 1] == 'x' and positions[i][j - 2] == '.':
                    return 'YES'
                elif positions[i][j] == '.' and positions[i][j - 1] == 'x' and positions[i][j - 2] == 'x':
                    return 'YES'
                elif positions[i][j] == 'x' and positions[i][j - 1] == '.' and positions[i][j - 2] == 'x':
                    return 'YES'
        
                elif i == 3:
                    if positions[i][j] == 'x' and positions[i - 1][j - 1] == 'x' and positions[i - 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i - 1][j - 1] == 'x' and positions[i - 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i - 1][j - 1] == '.' and positions[i - 2][j - 2] == 'x':
                        return 'YES'
                elif i == 0:
                    if positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j - 1] == '.' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                elif i == 1:
                    if positions[i][j] == 'x' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j - 1] == 'x' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j - 1] == '.' and positions[i + 2][j - 2] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == 'x' and positions[i + 2][j] == '.':
                        return 'YES'
                    elif positions[i][j] == '.' and positions[i + 1][j] == 'x' and positions[i + 2][j] == 'x':
                        return 'YES'
                    elif positions[i][j] == 'x' and positions[i + 1][j] == '.' and positions[i + 2][j] == 'x':
                        return 'YES'
    return 'NO'
test_cases = input()
for test_case in range(test_cases):
    positions = []
    for i in range(4):
        positions.append(raw_input())
    result = is_batman_wins(positions)
    print result