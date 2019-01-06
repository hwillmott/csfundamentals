class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        r = 1
        w = 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        return w