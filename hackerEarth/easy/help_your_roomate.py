test_cases = input()
for test_case in range(0, test_cases):
    num = input()
    count = 0
    while num:
        num = num & num - 1
        count += 1
    print count