class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = []
        self.size = size
        self.total = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            tmp = self.queue.pop()
            self.total -= tmp

        self.queue = [val] + self.queue
        self.total += val
        return float(self.total) / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)