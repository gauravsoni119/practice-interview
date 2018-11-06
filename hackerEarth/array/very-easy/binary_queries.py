N, Q = map(int, raw_input().split(' '))
arr = raw_input().split(' ')
for test_case in xrange(Q):
    query = map(int, raw_input().split(' '))
    if query[0] == 1:
        if arr[query[1] - 1] == '1':
            arr[query[1] - 1] = '0'
        else:
            arr[query[1] - 1] = '1'
    else:
        if arr[query[2] - 1] == '0':
            print 'EVEN'
        else:
            print 'ODD'