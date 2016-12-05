class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(result, nums, currlist, start):
            result.append(currlist)
            for i in range(start, len(nums)):
                backtrack(result, nums, currlist + [nums[i]], i+1)
        res = []
        backtrack(res, nums, [], 0)
        return res
        