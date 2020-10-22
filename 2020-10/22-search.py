﻿# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3503/

# Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

# You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.

# Example 1:

# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:

#     You may assume that all elements in the array are unique.
#     The value of each element in the array will be in the range [-9999, 9999].
#     The length of the array will be in the range [1, 10^4].


def search(reader, target):
    lo, hi = 0, 19999

    while lo <= hi:
        mid = (lo + hi) // 2
        val = reader.get(mid)

        if val > target or val == 2147483647:
            hi = mid - 1
        elif val < target:
            lo =  mid + 1
        else:
            return mid

    return -1



print(search([-1,0,3,5,8,99], 5)) # 3
print(search([-1,0,3,5,8,99], 4)) # -1