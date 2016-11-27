class Solution(object):
    def countBattleships2(self, board):
        def sinkShip(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == "X":
                board[i][j] = "."
                for k in range(i-1,i+2):
                    sinkShip(board, k, j)
                for l in range(j-1,j+2):
                    sinkShip(board, i, l)
            
        if board is None or len(board) == 0:
            return 0
        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    result += 1
                    sinkShip(board,i,j)
        return result
        
    def countBattleships(self, board):
        if board is None or len(board) == 0:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".": continue
                if i > 0 and board[i-1][j] == "X": continue
                if j > 0 and board[i][j-1] == "X": continue
                count += 1
        return count
        
                    