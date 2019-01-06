class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 0:
            return
        
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        nums = self.reverse(nums, i)
        if i > 0:
            k = i
            pivot = nums[i - 1]
            while k < len(nums) - 1 and nums[k] <= pivot:
                k += 1
            tmp = nums[k]
            nums[k] = nums[i - 1]
            nums[i - 1] = tmp   
        
    def reverse(self, ls, idx):
        first = idx
        last = len(ls) - 1
        while first < last:
            tmp = ls[first]
            ls[first] = ls[last]
            ls[last] = tmp
            first += 1
            last -= 1
        return ls