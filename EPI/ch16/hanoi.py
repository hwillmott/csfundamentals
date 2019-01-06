class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

def hanoi(numRings):
    pegs = [Stack(), Stack(), Stack()]
    for i in range(numRings - 1, -1, -1):
        pegs[0].push(i)
    
def hanoiSteps(

stack = Stack()
items = [9,8,7,6,5]
for i in items:
    stack.push(i)
print stack.items

hanoi(6)
