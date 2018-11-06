if __name__ == '__main__':
    str_list = raw_input()
    perm_list = []
    count = 0
    for i in range(len(str_list)):
        perm_list.append(0)
    print perm_list
    for i in range(len(str_list)):
        for j in range(len(str_list)):
            if str_list[i] == str_list[j]:
                perm_list[j] += 1
                break
    for i in perm_list:
        if count > 1:
            print 'not permutation of palindrome'
            break
        if i % 2 != 0:
            count += 1
    print perm_list
    if count == 0:
        print perm_list
        print 'permutation of palindrome'