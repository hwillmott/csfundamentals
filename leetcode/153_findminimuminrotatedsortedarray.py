class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hi = len(nums) - 1
        lo = 0
        
        while lo < hi:
            mid = lo + (hi-lo) / 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]