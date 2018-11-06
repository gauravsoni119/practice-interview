def blackjack(a, b, c):
    d = a + b + c
    if (d <= 21):
        return d
    elif d > 21 and (a == 11 or b == 11 or c == 11):
        return d - 10
    else:
        return 'BUST'
print blackjack(5,6,7)
print blackjack(9,9,9)
print blackjack(9,9,11)