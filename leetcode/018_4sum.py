class Solution(object):
    def fourSum(self, nums, target):
        def nSum(nums, target, n, result, results):
            if len(nums) < n or nums[0]*n > target or nums[-1]*n < target or n < 2:
                return
            if n == 2:
                i, j = 0, len(nums)-1
                while i < j:
                    s = nums[i] + nums[j]
                    if s == target:
                        results.append(result + [nums[i]] + [nums[j]])
                        i += 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                    elif s < target:
                        i += 1
                    else:
                        j -= 1
            else:
                for k in range(len(nums)-n+1):
                    if k == 0 or nums[k] != nums[k-1]:
                        nSum(nums[k+1:], target-nums[k], n-1, result+[nums[k]], results)
        results = []
        nSum(sorted(nums), target, 4, [], results)
        return results018_4sum