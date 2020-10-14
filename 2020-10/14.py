def rob(nums):
    def house_robber(nums):
        rob = not_rob = 0

        for num in nums:
            rob, not_rob = num + not_rob, max(rob, not_rob)

        return max(rob, not_rob)

    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))



print(rob([2, 3, 2])) # 3
print(rob([1, 2, 3, 1])) # 4
print(rob([1])) # 0
print(rob([1, 2, 4, 3, 3, 4, 6, 2, 2, 7, 1])) # 20?
              #  x     x     x        x