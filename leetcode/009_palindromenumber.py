class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        start = x
        result = 0
        while x:
            result *= 10
            result += x%10
            x /= 10
        return start == result
