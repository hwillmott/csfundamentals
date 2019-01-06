class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        l = len(num)-k
        
        for c in num:
            while stack and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        i = 0
        while i < l and stack[i] == '0': i += 1
        if i == l:
            return "0"
        else:
            return ''.join(stack[i:l])