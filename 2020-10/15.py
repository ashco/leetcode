def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)

    for _ in range(k):
        nums.insert(0, nums.pop())

    # left = nums[:-k]
    # right = nums[-k:]
    # nums = right + left

    print(nums)

print(rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]

