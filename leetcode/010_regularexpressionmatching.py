class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1,len(p)+1):
            if p[j-1] == "*": dp[0][j] = dp[0][j-1] or (j > 0 and dp[0][j-2])
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1] == ".": # char match
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == "*":
                    if p[j-2] != s[i-1] and p[j-2] != ".": # star matches empty
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
        return dp[-1][-1]