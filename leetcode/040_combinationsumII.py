class Solution(object):
    def backtrack(self, currlist, start, nums, target, result):
        if sum(currlist) == target:
            result.append(currlist)
        if sum(currlist) > target:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.backtrack(currlist + [nums[i]], i+1, nums, target, result)
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []
        self.backtrack([],0,candidates,target,result)
        return results