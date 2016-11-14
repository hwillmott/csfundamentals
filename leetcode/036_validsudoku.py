class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            used = [0 for x in range(9)]
            for j in range(9):
                num = ord(board[i][j]) - ord('1')
                if num >= 0 and num < 9:
                    if used[num] > 0:
                        return False
                    used[num] = 1
                    
        for i in range(9):
            used = [0 for x in range(9)]
            for j in range(9):
                num = ord(board[j][i]) - ord('1')
                if num >= 0 and num < 9:
                    if used[num] > 0:
                        return False
                    used[num] = 1
                    
        for i in range(3):
            for j in range(3):
                used = [0 for x in range(9)]
                for k in range(3):
                    for l in range(3):
                        num = ord(board[3*i+k][3*j+l]) - ord('1')
                        if num >= 0 and num < 9:
                            if used[num] > 0:
                                return False
                            used[num] = 1
        return True