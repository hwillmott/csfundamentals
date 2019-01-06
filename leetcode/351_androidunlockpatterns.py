class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def backtrack(visited, hops, curr, remaining):
            if remaining < 0: return 0
            if remaining == 0: return 1
            visited[curr] = True
            results = 0
            for i in range(1,10):
                if not visited[i] and (hops[curr][i] == 0 or visited[hops[curr][i]]):
                    results += backtrack(visited, hops, i, remaining-1)
            visited[curr] = False
            return results
                
        hops = [[0 for i in range(10)] for j in range(10)]
        hops[1][3] = hops[3][1] = 2
        hops[1][7] = hops[7][1] = 4
        hops[3][9] = hops[9][3] = 6
        hops[7][9] = hops[9][7] = 8
        hops[2][8] = hops[8][2] = hops[4][6] = hops[6][4] = hops[3][7] = hops[7][3] = hops[1][9] = hops[9][1] = 5
        
        visited = [False for i in range(10)]
        count = 0
        for i in range(m, n+1):
            count += backtrack(visited, hops, 1, i-1) * 4
            count += backtrack(visited, hops, 2, i-1) * 4
            count += backtrack(visited, hops, 5, i-1)
        return count