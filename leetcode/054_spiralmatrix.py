class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        startx = 0
        endx = len(matrix[0]) - 1
        starty = 0
        endy = len(matrix) - 1
        result = []
        while startx < endx and starty < endy:
            for i in range(startx, endx+1):
                result.append(matrix[starty][i])
            for i in range(starty+1, endy):
                result.append(matrix[i][endx])
            for i in range(startx, endx+1)[::-1]:
                result.append(matrix[endy][i])
            for i in range(starty+1, endy)[::-1]:
                result.append(matrix[i][startx])
            startx += 1
            endx -= 1
            starty += 1
            endy -= 1
        if startx == endx and starty == endy:
            result.append(matrix[starty][startx])
        elif startx == endx and starty < endy:
            for i in range(starty, endy+1):
                result.append(matrix[i][startx])
        elif starty == endy and startx < endx:
            for i in range(startx, endx+1):
                result.append(matrix[starty][i])
        return result