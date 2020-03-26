class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        temp = ""
        for i in range(len(s)):
            temp = self.helper(s, i, i) # odd length palindromes
            if len(temp) > len(longest):
                longest = temp
            temp = self.helper(s, i, i+1) # even length palindromes
            if len(temp) > len(longest):
                longest = temp
        return longest 
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
