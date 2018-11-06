def get_subsequence(num, N, s):
    sub = ''
    for i in range(0, N):
        if (num & (1<<i)):
            sub += s[i]
    return sub

test_cases = input()
for test_case in range(0, test_cases):
    s1 = raw_input()
    s2 = raw_input()
    sub_seq_s1 = []
    sub_seq_s2 = []
    len_of_s1 = len(s1)
    len_of_s2 = len(s2)
    for i in xrange(1, 2**len_of_s1):
        sub_seq_s1.append(get_subsequence(i, len_of_s1, s1))

    for j in xrange(1, 2**len_of_s2):
        sub_seq_s2.append(get_subsequence(j, len_of_s2, s2))
    if len((list(set(sub_seq_s1).intersection(set(sub_seq_s2))))) > 0:
        print 'Yes'
    else:
        print 'No'
