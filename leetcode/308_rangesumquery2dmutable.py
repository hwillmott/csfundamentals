class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: return;
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.tree = [[0 for i in range(self.n+1)] for j in range(self.m+1)]
        self.nums = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i,j,matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if self.m == 0 or self.n == 0: return
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row+1
        while i <= self.m:
            j = col+1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.m == 0 or self.n == 0: return 
        return self.sumTree(row2+1, col2+1) + self.sumTree(row1,col1) - self.sumTree(row1,col2+1) - self.sumTree(row2+1,col1)
        
    def sumTree(self, row, col):
        s = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)