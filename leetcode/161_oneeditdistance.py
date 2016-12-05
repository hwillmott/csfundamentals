class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens = len(s)
        lent = len(t)
        for i in range(min(lens,lent)):
            if s[i] != t[i]:
                if lens == lent:
                    return s[i+1:] == t[i+1:]
                elif lens < lent:
                    return s[i:] == t[i+1:]
                else:
                    return s[i+1:] == t[i:]
        return abs(lens-lent) == 1