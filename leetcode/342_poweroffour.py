class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: 
            return False
        if num & (num - 1) != 0:
            return False
        while num  != 0:
            if num == 1: 
                return True
            num = num >> 2
        return False