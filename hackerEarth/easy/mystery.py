val = raw_input().split('\n')
for num in val:
    num = int(num)
    if num == 0:
        print 0
        continue
    else:
        num = bin(num)
        output = ''
        for i in range(len(num) - 1, 0, -1):
            output = num[i] + output
            if num[i] == '1':
                break
        print int(output, 2)