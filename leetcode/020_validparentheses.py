class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        
        braces = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                braces.append(c)
            else:
                if len(braces) <= 0:
                    return False
                elif c == ')':
                    popped = braces.pop()
                    if popped != '(':
                        return False
                elif c == ']':
                    popped = braces.pop()
                    if popped != '[':
                        return False
                else: 
                    popped = braces.pop()
                    if popped != '{':
                        return False
        if len(braces) != 0:
            return False
        return True