class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peekMax(self):
        return self.items[len(self.items) - 1][1]

    def pop(self):
        if not self.isEmpty():
            self.items.pop()

    def push(self, item):
        if self.isEmpty():
            self.items.append((item, item))
        else:
            oldMax = self.peekMax()
            if item > oldMax:
                newMax = item
            else:
                newMax = oldMax
            self.items.append((item, newMax))

class auxStack:
    def __init__(self):
        self.items = []
        self.maxms = []

    def isEmpty(self):
        return self.items == []
    def peekMax(self):
        if not self.isEmpty():
            return self.maxms[len(self.maxms) - 1][0]
    def peekMaxCount(self):
        if not self.isEmpty():
            return self.maxms[len(self.maxms) - 1][1]
    def pop(self):
        if not self.isEmpty():
            item = self.items.pop()
            if item == self.peekMax():
                if self.peekMaxCount() > 1:
                    var = self.peekMaxCount()
                    self.maxms[len(self.maxms) - 1] = (item, var - 1)
                else:
                    self.maxms.pop()
    def push(self, item):
        if self.isEmpty():
            self.maxms.append((item, 1))
        else:
            oldMax = self.peekMax()
            if item == oldMax:
                var = self.peekMaxCount()
                self.maxms[len(self.maxms) - 1] = (item, var + 1)
            elif item > oldMax:
                self.maxms.append((item, 1))
        self.items.append(item)
