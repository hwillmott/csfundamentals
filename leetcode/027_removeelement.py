class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        writeIdx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[writeIdx] = nums[i]
                writeIdx += 1
        return writeIdx