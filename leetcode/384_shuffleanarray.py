from random import randrange
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.original = list(nums)
        self.arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.arr = list(self.original)
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in xrange(len(self.arr)):
            j = randrange(i, len(self.arr))
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()