class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        nums = sorted(nums)
        half = len(nums)//2
        currn = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                currn += 1
                if currn > half:
                    return nums[i]
            else:
                currn == 1
        return nums[0]