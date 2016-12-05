class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        bits = path.split("/")
        stack = []
        for b in bits:
            if b == "." or len(b) == 0: continue
            if b == "..":
                if len(stack) > 0: stack.pop()
                continue
            stack.append(b)
        if len(stack) == 0:
            return "/"
        res = ""
        for i in range(len(stack)):
            res += "/" + stack[i]
        return res