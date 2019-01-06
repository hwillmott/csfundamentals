class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return -1
        if len(nums) == 1: return 0
        
        for i in range(len(nums)):
            if 0 < i < len(nums)-1 and nums[i-1] < nums[i] > nums[i+1]:
                return i
            if i == 0 and nums[i+1] < nums[i]:
                return i
            if i == len(nums)-1 and nums[i-1] < nums[i]:
                return i
        