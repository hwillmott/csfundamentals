class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        strn = "1"
        
        for i in range(n - 1):
            tempStr = ""
            currIdx = 0
            readIdx = 0
            while readIdx < len(strn):
                count = 0
                while readIdx < len(strn) and strn[currIdx] == strn[readIdx]:
                    count += 1
                    readIdx += 1
                tempStr += str(count) + strn[currIdx]
                currIdx = readIdx
            strn = tempStr
            
        return strn