class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        top = len(nums) - 1
        bottom = 0
        
        while top >= bottom:
            middle = top - (top - bottom) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                top = middle - 1
            else:
                bottom = middle + 1
                
        return bottom