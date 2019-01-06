class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def addrange(res, lo, hi):
            if lo == hi:
                res.append(str(lo))
            else:
                res.append(str(lo)+"->"+str(hi))
        
        if nums is None: return []
        nxt = lower
        result = []
        if len(nums) == 0: 
            addrange(result, lower, upper)
            return result
        
        for i in xrange(len(nums)):
            if nums[i] < nxt: continue
            if nums[i] == nxt:
                nxt += 1
                continue
            addrange(result, nxt, nums[i]-1)
            nxt = nums[i] + 1
            
        if nxt <= upper:
            addrange(result, nxt, upper)
        return result