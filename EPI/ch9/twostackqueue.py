class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def push(self, item):
        self.items.append(item)

class TSQueue:
    def __init__(self):
        self.eStack = Stack()
        self.dStack = Stack()

    def enqueue(self, item):
        self.eStack.push(item)

    def dequeue(self):
        if self.dStack.isEmpty():
            self.transferStacks()
        if self.dStack.isEmpty():
            return None
        else:
            return self.dStack.pop()
        
    def isEmpty(self):
        return self.eStack.isEmpty() and self.dStack.isEmpty()

    def transferStacks(self):
        while not self.eStack.isEmpty():
            v = self.eStack.pop()
            self.dStack.push(v)


t = TSQueue()
for ch in "abcdef":
    t.enqueue(ch)

print(t.dequeue())
t.enqueue('g')
print(t.dequeue())

while not t.isEmpty():
    print(t.dequeue())
