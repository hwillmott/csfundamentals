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
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif sum <= 0:
                        j += 1
                    elif sum >= 0:
                        k -= 1
            i += 1
        return result