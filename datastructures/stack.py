class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def print(self):
        print(self.items)

myStack = Stack()
myStack.push(1)
myStack.push(3)
myStack.print()
print(myStack.pop())
print(myStack.pop())
