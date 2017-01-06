class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) < 2:
            return False
            
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                t = s[:i] + "--" + s[i+2:]
                if not self.canWin(t):
                    return True
        return False