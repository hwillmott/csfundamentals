class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        area = 0
        corners = set()
        for r in rectangles:
            x1 = min(x1, r[0])
            y1 = min(y1, r[1])
            x2 = max(x2, r[2])
            y2 = max(y2, r[3])
            
            area += (r[2]-r[0])*(r[3]-r[1])
            
            theseCorners = [(r[0],r[1]),(r[0],r[3]),(r[2],r[1]),(r[2],r[3])]
            
            for c in theseCorners:
                if c in corners:
                    corners.remove(c)
                else:
                    corners.add(c)
        if len(corners) != 4: return False
        outerCorners = [(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
        for o in outerCorners:
            if o not in corners: return False
        outerArea = (x2-x1)*(y2-y1)
        if outerArea != area: return False
        return True
            