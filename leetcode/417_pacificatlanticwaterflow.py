class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(matrix, i, j, results, mask):
            results[i][j] |= mask
            for k,l in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if k >= 0 and l >= 0 and k < len(matrix) and l < len(matrix[0]) and results[k][l] & mask == 0 and matrix[i][j] <= matrix[k][l]:
                        dfs(matrix,k,l,results,mask)
            
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        results = [[0 for _ in range(n)] for _ in range(m)]
        res = []
        for i in range(m):
            dfs(matrix, i, 0, results, 1)
            dfs(matrix, i, n-1, results, 2)
        for i in range(n):
            dfs(matrix, 0, i, results, 1)
            dfs(matrix, m-1, i, results, 2)
        print(results)
        for i in range(m):
            for j in range(n):
                if results[i][j] == 3:
                    res.append([i,j])
        return res
                    
            
        
        