class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        if len(self.mins) == 0 or self.getMin() >= x:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.items.pop()
        if tmp == self.getMin():
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[len(self.items)-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[len(self.mins)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()