class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        chrs = list(s)
        res = 0
        for c in chrs:
            res = res * 26
            num = ord(c) - ord('A') + 1
            res += num
        return res