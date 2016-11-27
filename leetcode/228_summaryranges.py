class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0:
            return result        
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] > 1:
                if nums[i-1] == start:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]
        if nums[-1] == start:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))
        return result