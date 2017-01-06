class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = 0
        masks = [0 for _ in range(len(words))]
        for i in range(len(words)):
            for c in words[i]:
                masks[i] |= 1 << (ord(c)-ord('a'))
            for j in range(i):
                if (masks[i] & masks[j]) == 0:
                    result = max(result, len(words[i])*len(words[j]))
        return result