class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        factor = 5
        sum = 0
        while factor <= n:
            sum += n / factor
            factor *= 5
        return sum