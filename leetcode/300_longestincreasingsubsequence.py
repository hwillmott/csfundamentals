class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        size = 0
        for n in nums:
            i,j = 0,size
            while i != j:
                m = (i+j)/2
                if dp[m] < n:
                    i = m + 1
                else:
                    j = m
            dp[i] = n
            size = max(i+1,size)
        return size