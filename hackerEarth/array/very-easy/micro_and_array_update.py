def is_greater_than_k(arr, K, N):
    flag = False
    for i in range(0, N):
        if arr[i] >= K:
            flag = True
        else:
            flag = False
            break
    return flag

test_cases = input()
for test_case in range(0, test_cases):
    N, K = map(int, raw_input().split(' '))
    arr = map(int, raw_input().split(' '))
    if is_greater_than_k(arr, K, N):
        print 0
    else:
        min_of_arr = min(arr)
        print K - min_of_arr
    # count = 0
    # if is_greater_than_k(arr, K, N):
    #     print count
    # else:
    #     is_greater = False
    #     while not is_greater:
    #         for i in range(0, N):
    #             arr[i] += 1
    #         count += 1
    #         is_greater = is_greater_than_k(arr, K, N)
    #     print count