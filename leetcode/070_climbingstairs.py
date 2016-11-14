class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        last = 1 # one stair
        current = 2 # two stairs
        
        for i in range(n-2):
            last, current = current, current + last
            
        return current