class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(nums, [], result)
        return result
       
    def backtrack(self, nums, currlist, result):
        if len(currlist) == len(nums):
            result.append(currlist)
            return
        for i in range(len(nums)):
            if nums[i] not in currlist: self.backtrack(nums, currlist+[nums[i]], result)