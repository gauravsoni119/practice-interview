def summer_69(arr):
    temp = 0
    skip = False
    for i in arr:
        if i == 6:
            skip = True
        elif i == 9:
            skip = False
        else:
            if skip == False:
                temp += i
    return temp

print summer_69([1, 3, 5])
print summer_69([4, 5, 6, 7, 8, 9])
print summer_69([2, 1, 6, 9, 11])
