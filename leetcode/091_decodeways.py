class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1: return 0 if s[0] == "0" else 1
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[1] == "0" else 1
        s = "0" + s
        for i in range(2,len(s)):
            if s[i] == 0: continue
            dp[i] = dp[i-1] + dp[i-2] if int(s[i-2:i+1]) <= 26 else dp[i-1]
        return dp[len(s)-1]