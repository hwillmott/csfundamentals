# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        result = 0 
        for i in range(len(points)-1):
            slopes = dict()
            vertical = 1
            same = 0
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1.x == p2.x:
                    if p1.y == p2.y:
                        same += 1
                    else:
                        vertical += 1
                else:
                    slope = (p2.y-p1.y)*1.0/(p2.x-p1.x)
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 2
            if len(slopes) > 0:
                local = reduce(max, slopes.values())
            else:
                local = 0
            local = max(same + vertical, same + local)
            result = max(local, result)
        return result