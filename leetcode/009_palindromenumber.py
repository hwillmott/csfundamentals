class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x < 10: return True
        if x % 10 == 0: return False
        
        v = 0
        while x - v > 0:
            v = v * 10 + x % 10
            x = x / 10
        if v > x:
            v = v / 10
        return v == x