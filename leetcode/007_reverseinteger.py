class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483647:
            return 0
        isNegative = x < 0
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x = x / 10
        if result > 2147483647 or result < -2147483647:
            return 0
        return -result if isNegative else result