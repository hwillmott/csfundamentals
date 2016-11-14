class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last = [1]
        for i in range(rowIndex):
            current = [1]
            for j in range(len(last)-1):
                current.append(last[j] + last[j+1])
            current.append(1)
            last = current
        return last