class Solution(object):
    def getPaths(self, paths, x, y):
        if x < 0 or y < 0:
            return 0
        return paths[x][y]
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    paths[0][0] = 1
                else:
                    paths[i][j] = self.getPaths(paths, i-1, j) + self.getPaths(paths, i, j-1)
        return paths[n-1][m-1]