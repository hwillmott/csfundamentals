from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = defaultdict(int)
        for c in t:
            d[c] += 1
        lo, hi, mins, minl, counter = 0,0,0,len(s)+1,len(t)
        while hi < len(s):
            if d[s[hi]] > 0:
                counter -= 1
            d[s[hi]] -= 1
            hi += 1
            while counter == 0:
                if hi-lo < minl:
                    mins = lo
                    minl = hi-lo
                d[s[lo]] += 1
                if d[s[lo]] > 0:
                    counter += 1
                lo += 1
        if minl < len(s)+1:
            return s[mins:mins+minl]
        return ""
        