class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        i = len(a) - 1
        j = len(b) - 1
        s = ""
        while i >= 0 or j >= 0 or c == 1:
            c += 0 if i<0 else ord(a[i]) - ord('0')
            c += 0 if j<0 else ord(b[j]) - ord('0')
            s = chr(c%2 + ord('0')) + s
            c = c/2
            i -= 1
            j -= 1
        return s