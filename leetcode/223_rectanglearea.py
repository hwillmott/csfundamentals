class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaA = (C-A)*(D-B)
        areaB = (G-E)*(H-F)
        
        left = max(A,E)
        top = min(D,H)
        right = min(C,G)
        bottom = max(B,F)
        
        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)
        else:
            overlap = 0
        return areaA + areaB - overlap