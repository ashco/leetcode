import collections

class Solution():
    # def twoSum(self, target, nums):
    #     d = {}
    #     for i, num in enumerate(nums):
    #         d[num] = i

    #     for i, num in enumerate(nums):
    #         remainder = target - num
    #         if remainder in d and d[remainder] != i:
    #             return [i, d[remainder]]

    #     return None
    def threeSum(self, nums):
        res = []

        for i, num in enumerate(nums):
            subNums = nums[:i] + nums[i + 1:]
            for subList in self.twoSums(num, subNums):
                print(-num, subList)

        # for i, num in enumerate(nums):
        #     subNums = nums[:i] + nums[i + 1:]
        #     for i1, i2 in self.twoSums(-num, subNums):
        #         print(num, i1, i2)
        #         res.append([nums[i1],nums[i2],num])




        return res



    def twoSums(self, target, nums):
        d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        res = []

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in d:
                # check that different index is present
                for index in d[remainder]:
                    if index < i:
                        res.append([index, i])
        return res





# print(Solution().twoSums(9, [4, 3, 7, 2, 55, -46, 12, 23, 4, 5, 6]))
print(Solution().threeSum([4, 3, 7, 2, 55, -46, 12, 23, 4, 5, 6, -4, -3, -2, -1, 0]))
                          #0  1  2  3  4   5    6    7  8  9  10 11  12  13  14  15