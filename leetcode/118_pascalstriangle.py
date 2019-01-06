class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        triangle = [[1]]
        for i in range(numRows-1):
            newRow = [1]
            for j in range(len(triangle[i])-1):
                newRow.append(triangle[i][j] + triangle[i][j+1])
            newRow.append(1)
            triangle.append(newRow)
        return triangle