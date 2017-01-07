class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def countWater(i,j,grid):
            s = 0
            for k,l in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0 <= k < len(grid) and 0 <= l < len(grid[0]):
                    if grid[k][l] == 0: s += 1
                else:
                    s += 1
            return s
            
        def dfs(grid,i,j,visited):
            visited[i][j] = True
            s = countWater(i,j,grid)
            for k,l in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and visited[k][l] == False and grid[k][l] == 1:
                    s += dfs(grid,k,l,visited)
            return s
        
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j,visited)
                    
                    
                    