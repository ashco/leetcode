class Solution():
    # def __init__(self):
    #     pass
    def closestSum(self, list1, list2, target):
        # return closest sum to target from 1 num in each array

        list1.sort()
        list2.sort()

        p1, p2 = 0, len(list2) - 1

        res = float('inf')

        while p1 < len(list1) and p2 > 0:
            numSum = list1[p1] + list2[p2]  # 19 9 4

            if abs(numSum - target) < abs(res - target):
                res = numSum

            if numSum == target:
                return target
            elif numSum < target:
                p1 += 1
            else:
                p2 -= 1

        return res



list1 = [-21,3,8,2,9,5, 33, 2, 11, 54]   # -1 2 3 5 8 9
                                # 1
list2 = [4,1,2,100,5,20]  # 1 2 4 5 10 20
                                #  2


print(Solution().closestSum(list1, list2, 44))



