class Solution(object):
    def backtrack(self, candidates, idx, currlist, currsum, target, result):
        if currsum == target:
            result.append(currlist)
            return
        if currsum > target:
            return
        for i in range(idx,len(candidates)):
            self.backtrack(candidates, i, currlist + [candidates[i]], currsum+candidates[i], target, result)
    
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(candidates, 0, [], 0, target, result)
        return result