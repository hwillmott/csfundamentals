class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        s = " " + s
        for i in range(1,len(s)):
            for j in range(i-1,-1,-1):
                if dp[j]:
                    word = s[j+1:i+1]
                    if word in wordDict:
                        dp[i] = True
        return dp[len(s)-1]