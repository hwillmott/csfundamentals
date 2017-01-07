class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0: return 0
        d = dict()
        for i in range(len(s)):
            if s[i] in d: 
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        usedOdd = False
        count = 0
        for k,v in d.items():
            if v%2 == 1:
                if not usedOdd:
                    count += v
                    usedOdd = True
                else:
                    count += v-1
            else:
                count += v
                
        return count