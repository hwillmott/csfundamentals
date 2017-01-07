class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.children = dict()

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        root = TrieNode(0)
        for num in nums:
            curr = root
            for i in range(32)[::-1]:
                curbit = (num >> i) & 1
                if curbit not in curr.children:
                    curr.children[curbit] = TrieNode(curbit)
                curr = curr.children[curbit]
        maximum = 0
        for num in nums:
            curr = root
            cursum = 0
            for i in range(32)[::-1]:
                curbit = (num >> i) & 1
                if curbit^1 in curr.children:
                    cursum |= 1 << i
                    curr = curr.children[curbit^1]
                else:
                    curr = curr.children[curbit]
            maximum = max(cursum, maximum)
        return maximum