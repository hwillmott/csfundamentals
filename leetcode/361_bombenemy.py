class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = 0 if m == 0 else len(grid[0])
        
        result = 0
        rowhits = 0
        colhits = [0 for i in range(n)]
        
        for i in xrange(m):
            for j in xrange(n):
                if not j or grid[i][j-1] == 'W':
                    rowhits = 0
                    for k in xrange(j,n):
                        if grid[i][k] == 'W': break
                        rowhits += grid[i][k] == 'E'
                if not i or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    for k in xrange(i,m):
                        if grid[k][j] == 'W': break
                        colhits[j] += grid[k][j] == 'E'
                if grid[i][j] == '0':
                    result = max(result, rowhits + colhits[j])
        return result