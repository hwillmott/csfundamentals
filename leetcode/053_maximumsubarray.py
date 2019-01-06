class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        last = nums[0]
        m = last
        for n in nums[1:]:
            if last > 0:
                last = last + n
            else:
                last = n
            if last > m:
                m = last
        return m
                