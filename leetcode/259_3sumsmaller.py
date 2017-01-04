class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 3: return 0
        nums = sorted(nums)
        count = 0
        
        for k in range(len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j-i
                    i += 1
                else:
                    j -= 1
                    
        return count