class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, len(nums)-1
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        for i in range(len(nums))[::-1]:
            if nums[i] < 1:
                break
            if nums[i] > 1:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
        
            