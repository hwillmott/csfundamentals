class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        currLen = 0
        for i in range(0, len(s)):
            if self.isPali(s, i - currLen - 1, i):
                result = s[i - currLen - 1: i + 1]
                currLen = currLen + 2
            elif self.isPali(s, i - currLen, i):
                result = s[i - currLen: i + 1]
                currLen = currLen + 1
        return result
            
    def isPali(self, s, start, end):
        if start < 0:
            return False
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True