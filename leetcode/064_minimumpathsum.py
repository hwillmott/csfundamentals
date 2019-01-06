class Solution(object):
    
    def getDist(self, dist, x, y):
        if x < 0 or y < 0:
            return float("inf")
        return dist[x][y]
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0
        dist = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if x == 0 and y == 0:
                    dist[0][0] = grid[0][0]
                else:
                    dist[x][y] = min(self.getDist(dist, x-1, y), self.getDist(dist, x, y-1)) + grid[x][y]
        return dist[len(grid)-1][len(grid[0])-1]