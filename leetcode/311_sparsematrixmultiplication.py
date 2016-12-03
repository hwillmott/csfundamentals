class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        arow = len(A)
        acol = len(A[0])
        bcol = len(B[0])
        
        res = [[0 for x in range(bcol)] for y in range(arow)]
        
        for i in range(arow):
            for k in range(acol):
                if A[i][k] != 0:
                    for j in range(bcol):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
        return res