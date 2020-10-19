class Solution():
    def validParenthisis(self, string):
        lookup = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        stack = []

        for char in string:
            if char in lookup:
                stack.append(lookup[char])
            elif char != stack.pop():
                return False
        return len(stack) == 0



string1 = '{(){{}}[]}'   # true
string2 = '{(){{}))'     # false
string3 = '[][][]{{}()}' # true
print(Solution().validParenthisis(string1))
print(Solution().validParenthisis(string2))
print(Solution().validParenthisis(string3))