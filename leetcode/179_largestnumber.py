class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(map(str, nums), lambda x,y: int(x+y)-int(y+x), reverse=True)
        r = ''.join(nums)
        return r.lstrip('0') or '0'