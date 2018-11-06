from collections import Counter
test_cases = input()
for test_case in range(test_cases):
    N = input()
    arr = map(int, raw_input().split())
    Q = input()
    arr = Counter(arr)
    for qr in xrange(Q):
        num = input()
        try:
            elem = len(arr) - 1 - arr[::-1].index(num)
            print elem + 1
        except:
            print -1