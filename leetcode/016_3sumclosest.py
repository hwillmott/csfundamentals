class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: 
            return sumList(nums)
            
        nums = sorted(nums)
        currSum = reduce(lambda x,y: x+y , nums[0:3])
        closest = currSum
        for i in range(1,len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i] + nums[j] + nums[k] 
                if abs(target-s) < abs(target-closest):
                    closest = s
                    if closest == target: return closest
                if s > target:
                    k -= 1
                else:
                    j += 1
        return closest