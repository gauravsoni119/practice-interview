def spy_game(nums):
    pattern = [0, 0, 7]
    for i in range(0, len(nums)):
        if len(pattern) and nums[i] == pattern[0]:
            del pattern[0]
    if len(pattern) == 0:
        return True
    else:
        return False

print spy_game([1,2,4,0,0,7,5])
print spy_game([1,0,2,4,0,5,7])
print spy_game([1,7,2,0,4,5,0])