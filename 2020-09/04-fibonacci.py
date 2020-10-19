# return n character of fibonacci sequence

# 0 1 1 2 3 5 8 13 21 34

class Solution():
    def __init__(self):
        self.cache = {
            0: 0,
            1: 1
        }

    def fibonacci(self, n):
        if n in self.cache: return self.cache[n]

        res = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        self.cache[n] = res

        return res


# class Solution():
#     def fibonacci(self, n):
#         if n <= 1: return n

#         return self.fibonacci(n - 1) + self.fibonacci(n - 2)




print(Solution().fibonacci(99)) # 3