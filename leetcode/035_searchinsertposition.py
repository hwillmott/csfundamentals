class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums[0] >= target:
            return 0
        r = 1
        while r < len(nums):
            if nums[r] >= target:
                return r
            r += 1
        return r