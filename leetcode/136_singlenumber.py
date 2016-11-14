class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            i = i + 2
        return nums[-1]