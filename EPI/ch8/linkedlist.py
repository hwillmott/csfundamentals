from Node import Node

class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def prepend(self, node):
        if self.head == None:
            self.tail = node
            self.head = node
        else:
            node.nxt = self.head
            self.head = node

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node

    def insert(self, value):
        n = Node(value)
        self.append(n)

    def insertMultiple(self, values):
        for v in values:
            self.insert(v)

    def prnt(self):
        currptr = self.head
        if self.head == None:
            print("->")
            return
        while currptr.nxt:
            print(str(currptr.value) + "->", end="")
            currptr = currptr.nxt
        print(currptr.value)
