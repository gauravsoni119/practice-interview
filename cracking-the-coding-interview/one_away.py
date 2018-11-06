def is_one_edit_away(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
            if count > 1:
                return False

def is_one_edit_away_insert(str1, str2):
    index1 = 0
    index2 = 0
    while(index2 < len(str2) and index1 < len(str1)):
        if str2[index2] != str1[index1]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True
if __name__ == '__main__':
    str1 = raw_input()
    str2 = raw_input()
    if len(str1) == len(str2):
        is_one_edit = is_one_edit_away(str1, str2)
        print is_one_edit
    else:
        is_one_edit = is_one_edit_away_insert(str1, str2)
        print is_one_edit