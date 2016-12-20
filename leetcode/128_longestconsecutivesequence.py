class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in s:
                m = n+1
                while m in s:
                    m += 1
                longest = max(longest, m-n)
        return longest 