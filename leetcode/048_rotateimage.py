class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None: return None
        n = len(matrix)
        start = 0
        end = n-1
        while start < end:
            for i in range(n):
                matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
            start += 1
            end -= 1
        for i in range(1,n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]