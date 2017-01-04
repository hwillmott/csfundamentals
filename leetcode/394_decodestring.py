class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        currstr = ''
        stack = []
        
        for c in s:
            if c == '[':
                stack.append(currstr)
                stack.append(count)
                currstr = ""
                count = 0
            elif c == ']':
                num = stack.pop()
                lastword = stack.pop()
                currstr = lastword + int(num)*currstr
            elif c.isdigit():
                count = count * 10 + int(c)
            else:
                currstr += c
        return currstr