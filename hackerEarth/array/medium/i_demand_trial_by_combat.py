test_cases = input()
for test_case in range(test_cases):
    n,m = map(int, raw_input().split())
    arr = raw_input().split()
    temp = arr[:]
    init_arr = arr[:]
    temp1 = []
    arr_len = len(arr)
    count = 0
    while count != m:
        for i in xrange(arr_len):
            if i == 0:
                if arr[i + 1] == '1':
                    temp[i] = '1'
                else:
                    temp[i] = '0'
            elif i == arr_len - 1:
                if arr[i - 1] == '1':
                    temp[i] = '1'
                else:
                    temp[i] = '0'
            else:
                if arr [i + 1] == '1' and arr[i - 1] == '1':
                    temp[i] = '1'
                else:
                    temp[i] = '0'
        if count == 0:
            temp1 = temp[:]
        if count > 1 and cmp(temp, temp1) == 0:
            temp = init_arr
            break
        arr = temp[:]
        count += 1
        print '.................', arr, temp, arr.count('1')
        if arr.count('1') == arr_len:
            break
        elif arr.count('0') == arr_len:
            break
    print (' ').join(temp)