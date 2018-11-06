prime_lis = []
num = int(raw_input())
for i in range(2, num):
    prime = True
    for j in range(2, i):
        # print j, i, i % j   
        if (i % j) == 0:
            prime = False
    if prime:
        prime_lis.append(str(i))
print " ".join(prime_lis)