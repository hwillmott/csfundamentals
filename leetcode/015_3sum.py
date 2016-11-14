class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = []
        i = 0
        nums.sort()
        while i < len(nums) - 2:
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                if sum <= 0:
                    while nums[j] == nums[j + 1] and j < k:
                        j = j + 1
                if sum >= 0:
                    while nums[k] == nums[k - 1] and j < k:
                        k = k - 1
            i += 1
        return result