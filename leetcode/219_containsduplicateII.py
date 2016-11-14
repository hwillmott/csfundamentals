class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i in range(len(nums)):
            if i > k:
                s.remove(nums[i-k-1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False