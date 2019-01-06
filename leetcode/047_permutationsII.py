class Solution(object):
    def backtrack(self, nums, used, currlist, result):
        if len(currlist) == len(nums):
            result.append(currlist)
            return 
        for i in range(len(nums)):
            if used[i] or (i>0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            self.backtrack(nums, used, currlist+[nums[i]], result)
            used[i] = False
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        used = [False] * len(nums)
        self.backtrack(nums, used, [], result)
        return result