class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        m = 0
        d = dict()
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                m = i + 1
            elif s-k in d:
                m = max(m, i - d[s-k])
            if s not in d:
                d[s] = i
        return m