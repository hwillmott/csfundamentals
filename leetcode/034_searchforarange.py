class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) == 0:
            return [-1,-1]
            
        top = len(nums) - 1
        bottom = 0
        found = False
        
        while top >= bottom:
            middle = top - (top - bottom) / 2
            print(middle)
            if nums[middle] == target:
                found = True
                break
            elif nums[middle] < target:
                bottom = middle + 1
            else:
                top = middle - 1
        if not found:
            return [-1,-1]
            
        lowerB = middle
        lowerTop = middle - 1
        while lowerTop >= bottom:
            newM = lowerTop - (lowerTop - bottom) / 2
            if nums[newM] < target:
                bottom = newM + 1
            else:
                lowerTop = newM - 1
                lowerB = newM
        
        upperB = middle
        upperBottom = middle + 1
        while top >= upperBottom:
            newM = top - (top - upperBottom) / 2
            if nums[newM] > target:
                top = newM - 1
            else:
                upperBottom = newM + 1
                upperB = newM
                
        return [lowerB, upperB]