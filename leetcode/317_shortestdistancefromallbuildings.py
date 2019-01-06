class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0: return -1
        buildings = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append([i,j])
        distances = [[0 for _ in range(n)] for _ in range(m)]
        bCount = len(buildings)
        for i in range(bCount):
            self.bfs(buildings[i][0],buildings[i][1],m,n,distances,grid,i)
        minDist = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -bCount and (minDist == -1 or minDist > distances[i][j]):
                    minDist = distances[i][j]
        return minDist
        
        
    def bfs(self,i,j,m,n,distances,grid,b):
        queue = [[i,j,0]]
        while queue:
            place = queue[0]
            queue = queue[1:]
            distances[place[0]][place[1]] += place[2]
            for k,l in [[place[0]+x,place[1]+y] for x,y in [(1,0),(-1,0),(0,1),(0,-1)]]:
                if 0 <= k < m and 0 <= l < n and grid[k][l] == -b:
                    grid[k][l] = -(b+1)
                    queue.append([k,l,place[2]+1])
            