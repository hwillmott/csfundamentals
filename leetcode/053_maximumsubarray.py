class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        maximum = dp[0]
        for i in range(1,length):
            if dp[i-1] > 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            maximum = max(maximum, dp[i])
        return maximum