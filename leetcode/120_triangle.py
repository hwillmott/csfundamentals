class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == [[]]: return 0
        triangle.sort(key=len, reverse=True)
        for i in range(len(triangle)-1):
            for j in range(len(triangle[i])-1):
                triangle[i+1][j] += min(triangle[i][j], triangle[i][j+1])
        return triangle[-1][0]