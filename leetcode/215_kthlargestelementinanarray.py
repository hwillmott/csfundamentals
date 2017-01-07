class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quickselect(nums, lo, hi, k):
            if lo > hi: return -1
            pivot = nums[hi]
            i = lo
            for j in range(lo,hi):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            
            if i == k: return nums[i]
            elif i > k: return quickselect(nums, lo, i-1, k)
            else: return quickselect(nums, i+1, hi, k)
        
        return quickselect(nums, 0, len(nums)-1, len(nums)-k)
            