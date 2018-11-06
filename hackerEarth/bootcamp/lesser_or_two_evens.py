def lesser_or_even(a, b):
    if (a % 2 == 0 and b % 2 == 0):
        return min(a, b)
    elif (a % 2 != 0 or b % 2 != 0):
        return max(a, b)
print lesser_or_even(2, 4)
print lesser_or_even(2, 5)