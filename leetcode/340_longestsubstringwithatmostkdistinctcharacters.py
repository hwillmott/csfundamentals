class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s is None: return 0
        if k == 0: return 0
        if len(s) <= k: return len(s)
        
        letterCounts = dict()
        lo = 0
        uniqueLetters = 0
        maximum = 0
        for i in range(len(s)):
            if s[i] not in letterCounts or letterCounts[s[i]] == 0:
                uniqueLetters += 1
                letterCounts[s[i]] = 1
            else:
                letterCounts[s[i]] += 1
            while uniqueLetters > k:
                if letterCounts[s[lo]] == 1:
                    uniqueLetters -= 1
                letterCounts[s[lo]] -= 1
                lo += 1
            maximum = max(maximum, i-lo+1)
        return maximum