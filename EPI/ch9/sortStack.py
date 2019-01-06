class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def printStack(self):
        while not self.isEmpty():
            print(str(self.pop()))

def srt(stack):
    if not stack.isEmpty():
        v = stack.pop()
        stack = srt(stack)
        stack = insrt(v, stack)
    return stack

def insrt(v, stack):
    if stack.isEmpty() or stack.peek() < v:
        stack.push(v)
    else:
        f = stack.pop()
        insrt(v, stack)
        s.push(f)
    return stack

s = Stack()
s.push(2)
s.push(4)
s.push(1)
s.push(7)
s.push(3)
s.push(8)
s.push(5)

s = srt(s)
s.printStack()
