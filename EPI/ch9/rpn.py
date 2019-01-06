class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def push(self, item):
        self.items.append(item)

def evaluateRPN(strn):
    intermediates = Stack()
    for ch in strn:
        if ch == '+':
            var1 = int(intermediates.pop())
            var2 = int(intermediates.pop())
            intermediates.push(var1 + var2)
        elif ch == '-':
            var1 = int(intermediates.pop())
            var2 = int(intermediates.pop())
            intermediates.push(var2 - var1)
        elif ch == '*':
            var1 = int(intermediates.pop())
            var2 = int(intermediates.pop())
            intermediates.push(var1 * var2)
        elif ch == '/':
            var1 = int(intermediates.pop())
            var2 = int(intermediates.pop())
            intermediates.push(var2 / var1)
        else:
            intermediates.push(ch)
    print intermediates.pop()

evaluateRPN("23+3*")


