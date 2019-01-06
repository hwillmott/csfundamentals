class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0 for i in range(n + 1)]
        ways[0] = 1
        ways[1] = 1
        
        for i in range(2, n + 1):
            s = 0
            for j in range(1, i+1):
                s += ways[j - 1] * ways[i - j]
            ways[i] = s
        return ways[n]