class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff  = 0
        for n in nums:
            diff ^= n
        diff &= ~(diff-1)
        res = [0,0]
        for n in nums:
            if n & diff:
                res[0] ^= n
            else:
                res[1] ^= n
        return res