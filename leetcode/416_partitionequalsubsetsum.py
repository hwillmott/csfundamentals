class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return True
            
        summ = sum(nums)
        if summ % 2 != 0:
            return False
            
        summ = summ / 2
        canPartition = [False for i in range(summ + 1)]
        canPartition[0] = True
        
        for i in range(1,len(nums)):
            for j in range(summ, nums[i-1]-1, -1):
                canPartition[j] = canPartition[j] or canPartition[j - nums[i-1]]
        return canPartition[summ]