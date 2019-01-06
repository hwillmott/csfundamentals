class Leaf:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, value, nxt=None, prev=None):
        self.value = value
        self.nxt = nxt
        self.prev = prev


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def push(self, item):
        if item.value is not None:
            print("pushing " + str(item.value.value))
            self.count += 1
            if self.head == None:
                self.tail = item
                self.head = item
            else:
                item.nxt = self.head
                self.head.prev = item
                self.head = item

    def pop(self):
        self.count -= 1
        if self.head is not None:
            print("popping " + str(self.head.value.value))
            n = self.head
            if self.count != 0:
                self.head = self.head.nxt
                self.head.prev = None
            else:
                self.head = None
            return n
        else: 
            return None

    def inject(self, item):
        if item.value is not None:
            self.count += 1
            if self.head == None:
                self.head = item
                self.tail = item
            else:
                self.tail.nxt = item
                item.prev = self.tail
                self.tail = item

    def eject(self):
        self.count -= 1
        if self.tail is not None:
            n = self.tail
            self.tail = self.tail.prev
            self.tail.nxt = None
            return n
        else:
            return None

    def printQueue(self):
        curr = self.head
        strn = ""
        while curr:
            strn += str(curr.value) + "->"
            curr = curr.nxt
        print strn

def inOrder(root):
    buff = Queue()
    level = []
    result = []
    buff.push(Node(root))
    count = 1 
    while not buff.isEmpty():
        curr = buff.pop().value
        count -= 1
        if curr is not None:
            level.append(curr.value)
            buff.inject(Node(curr.left))
            buff.inject(Node(curr.right))
        
        if count == 0:
            print("Count = 0")
            count = buff.size()
            result.append(level)
            level = []
    print result

#q = Queue()
#q.push(Node('a'))
#q.push(Node('b'))
#q.push(Node('c'))
#q.push(Node('d'))
#q.inject(Node('e'))
#q.inject(Node('f'))
#q.inject(Node('g'))
#q.inject(Node('h'))
#q.pop()
#q.eject()
#q.printQueue()

leafA = Leaf('a')
leafB = Leaf('b')
leafC = Leaf('c')

leafA.left = leafB
leafA.right = leafC

leafD = Leaf('d')
leafE = Leaf('e')

leafB.left = leafD
leafB.right = leafE

leafF = Leaf('f')
leafG = Leaf('g')
leafH = Leaf('h')
leafI = Leaf('i')

leafE.right = leafF
leafC.left = leafG
leafG.right = leafH
leafH.right = leafI

inOrder(leafA)
