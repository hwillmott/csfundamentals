class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = dict()
        while n not in d:
            d[n] = 0
            newSum = 0
            while n > 0:
                remain = n%10
                newSum += remain*remain
                n /= 10
            if newSum == 1:
                return True
            n = newSum
        return False