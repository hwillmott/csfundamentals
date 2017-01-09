class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return -1
        last = nums[0]
        m = last
        for i in range(1,len(nums)):
            if last > 0:
                last = last + nums[i]
            else:
                last = nums[i]
            if last > m:
                m = last
        return m
                