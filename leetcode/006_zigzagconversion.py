class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        rows = ["" for x in range(numRows)]
        i = 0
        if numRows == 1: 
            return s
        while i < len(s):
            for idx in range(numRows):
                if i < len(s):
                    rows[idx] += s[i]
                    i += 1
            for idx in range(numRows - 2, 0, -1):
                if i < len(s):
                    rows[idx] += s[i]
                    i += 1
        
        for j in range(numRows):
            result += rows[j]
            
        return result