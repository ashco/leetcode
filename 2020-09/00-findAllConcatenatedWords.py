class Solution(object):
    def findAllConcatenatedWords(self, words):
        wordDict = set(words)
        cache = {}
        return [word for word in words if self._canForm(word, wordDict, cache)]

    def _canForm(self, word, wordDict, cache):
        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in wordDict:
                if suffix in wordDict or self._canForm(suffix, wordDict, cache):
                    cache[word] = True
                    return True
        cache[word] = False
        return False


input = ['cat', 'cats', 'dog', 's', 'catsdog']
print(Solution().findAllConcatenatedWords(input))