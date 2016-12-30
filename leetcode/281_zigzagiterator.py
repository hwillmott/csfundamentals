class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = []
        if len(v1) > 0:
            self.lists.append(v1)
        if len(v2) > 0:
            self.lists.append(v2)
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        if len(self.lists) == 0: return -1
        tmp = self.lists[self.idx][0]
        if len(self.lists[self.idx]) > 1:
            self.lists[self.idx] = self.lists[self.idx][1:]
            self.idx += 1
            self.idx %= len(self.lists)
        else:
            del self.lists[self.idx]
            if self.idx == len(self.lists):
                self.idx = 0
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lists) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())