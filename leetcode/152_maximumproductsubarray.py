class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        lastmax = nums[0]
        lastmin = nums[0]
        maxsofar = nums[0]
        for i in range(1,len(nums)):
            thismax = max(nums[i], max(lastmax*nums[i], lastmin*nums[i]))
            thismin = min(nums[i], min(lastmax*nums[i], lastmin*nums[i]))
            maxsofar = max(thismax, maxsofar)
            lastmax = thismax
            lastmin = thismin
        return maxsofar