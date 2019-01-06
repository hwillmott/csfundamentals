class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k
        diff = k*(k-1)
        same = k
        for i in range(n-2):
            same, diff = diff, (same + diff)*(k-1)
        return same+diff
        