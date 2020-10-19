class Solution(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def isValidCords(self, i, j):
        return 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0])

    def dfs(self, i, j, target):
        if not self.isValidCords(i, j):
            return 0

        # mark matches negative
        val = self.matrix[i][j]

        if val == target:
            self.matrix[i][j] = -val

            res = 0
            # recursively run on side nodes
            for n_i, n_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                res += self.dfs(i + n_i, j + n_j, target)

            return res + 1
        else:while node:
    print(node.val)
    node = node.next
            return 0


    def maxConnectedColors(self):
        maxSum = 0

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                val = matrix[i][j]
                if val > 0:
                    newSum = self.dfs(i, j, val)
                    maxSum = max(newSum, maxSum)

        return maxSum



matrix = [
[3, 3, 1, 2],
[3, 1, 2, 1],
[2, 1, 2, 1],
[2, 1, 4, 1],
]
print(Solution(matrix).maxConnectedColors())