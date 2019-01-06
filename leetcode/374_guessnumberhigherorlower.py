# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        top = n
        bottom = 0
        middle = (top - bottom) / 2
        result = guess(middle)
        while result:
            if result < 0:
                top = middle - 1
            else:
                bottom = middle + 1
            middle = ((top - bottom) / 2) + bottom
            result = guess(middle)
        return middle