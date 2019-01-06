class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v2d = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            tmp = self.v2d[self.i][self.j] 
            self.j += 1
            return tmp
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.v2d) and self.j == len(self.v2d[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.v2d)
            

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())