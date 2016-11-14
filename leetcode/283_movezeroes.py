class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        readx = 0
        writex = 0
        while readx < len(nums):
            if nums[readx] != 0:
                nums[writex] = nums[readx]
                writex += 1
            readx += 1
        while writex < len(nums):
            nums[writex] = 0
            writex += 1