class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        writeIdx = 0
        readIdx = 0
        
        while readIdx < len(nums):
            if nums[readIdx] == nums[writeIdx]:
                readIdx += 1
            else:
                writeIdx += 1
                nums[writeIdx] = nums[readIdx]
                readIdx += 1
                
        return writeIdx + 1