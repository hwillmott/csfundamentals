class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.getLiveNeighbors(m, n, i, j, board)
                if board[i][j] & 1 == 1:
                    if lives == 3 or lives == 2:
                        board[i][j] = 3
                else:
                    if lives == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        
    def getLiveNeighbors(self, m, n, i, j, board):
        count = 0
        for k in range(max(0, i-1), min(i+1,m-1)+1):
            for l in range(max(0,j-1),min(j+1,n-1)+1):
                count += board[k][l] & 1
        count -= board[i][j] & 1
        return count