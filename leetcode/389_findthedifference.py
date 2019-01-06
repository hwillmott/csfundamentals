class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = 0
        for c in s:
            d ^= ord(c)
        for c in t:
            d ^= ord(c)
        return chr(d)