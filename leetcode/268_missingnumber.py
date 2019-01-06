class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in range(len(nums)):
            result ^= nums[i]
            result ^= i
        return result