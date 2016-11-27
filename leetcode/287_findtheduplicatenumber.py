class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow