class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        idx = 1
        carry = 0
        res = ""
        while idx <= len(a) or idx <= len(b):
            s = carry
            if idx <= len(a):
                aVal = 1 if a[-idx] == "1" else 0
                s += aVal
            if idx <= len(b):
                bVal = 1 if b[-idx] == "1" else 0
                s += bVal
            if s == 3:
                res = "1" + res
                carry = 1
            elif s == 2:
                res = "0" + res
                carry = 1
            elif s == 1:
                res = "1" + res
                carry = 0
            else:
                res = "0" + res
                carry = 0
            idx += 1
        if carry:
            res = "1" + res
        return res