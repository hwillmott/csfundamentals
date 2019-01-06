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
        if item is not None:
            self.items.append(item)

class Node:
    def __init__(self, value=None, nxt=None, jmp=None):
        self.value = value
        self.nxt = nxt
        self.jmp = jmp
        self.jmpord = -1

class posting:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, node):
        if head is None:
            head = node
        else:
            tmp = head
            head = node
            head.nxt = tmp

def setJumpOrderRecursive(head, order):
    if head and head.jmpord == -1:
        head.jmpord = order
        order = order + 1
        order = setJumpOrderRecursive(head.jmp, order)
        order = setJumpOrderRecursive(head.nxt, order)
    return order

def setJumpOrderIterative(head):
    s = Stack()
    order = 0
    s.push(head)
    while not s.isEmpty():
        curr = s.pop()
        if curr.jmpord == -1:
            curr.jmpord = order
            order += 1
            s.push(curr.nxt)
            s.push(curr.jmp)

def printPosting(head):
    curr = head
    while curr:
        print(curr.value + " " + str(curr.jmpord))
        curr = curr.nxt


nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')

nodeA.nxt = nodeB
nodeB.nxt = nodeC
nodeC.nxt = nodeD

nodeA.jmp = nodeC
nodeB.jmp = nodeD
nodeC.jmp = nodeB
nodeD.jmp = nodeD

p = posting(nodeA)

setJumpOrderIterative(nodeA)
printPosting(nodeA)
