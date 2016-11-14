class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        strs = self.parenHelper([], "", 0, 0, n)
        return strs
        
        
    def parenHelper(self, strs, strn, openP, closeP, mx):
        if len(strn) == mx * 2:
            strs.append(strn)
            return strs
            
        if openP < mx:
            strs = self.parenHelper(strs, strn + "(", openP + 1, closeP, mx)
        if closeP < openP:
            strs = self.parenHelper(strs, strn + ")", openP, closeP + 1, mx)
        return strs