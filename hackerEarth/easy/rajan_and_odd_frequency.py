test_cases = input()
for test_case in range(0, test_cases):
    n = input()
    arr = map(int, raw_input().split(' '))
    res = 0
    for i in arr:
        res = res ^ i
    if res:
        print res
    else:
        print -1