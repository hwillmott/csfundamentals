class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
            
        indices = [-1 for i in range(len(s) + 1)]
        
        for i in range(len(s)):
            if i > 0 and indices[i] == -1:
                return False
            for j in xrange(indices[i] + 1, len(t)):
                if t[j] == s[i]:
                    indices[i + 1] = j
                    break
        return True if indices[len(s)] >= 0 else False