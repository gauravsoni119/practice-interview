def find_33(nums):
    for i in range(0, len(nums) - 1):
        if nums [i] == 3 and nums[i + 1] == 3:
            return True
    else:
        return False

print find_33([1, 3, 3])
print find_33([1, 3, 1, 3])
print find_33([3, 1, 3])