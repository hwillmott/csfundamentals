class Solution(object):
    def getPaths(self, paths, grid, x, y):
        if x < 0 or y < 0 or grid[x][y] == 1:
            return 0
        return paths[x][y]
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        paths = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = self.getPaths(paths, obstacleGrid, i-1, j) + self.getPaths(paths, obstacleGrid, i, j-1)

        return paths[m - 1][n - 1]