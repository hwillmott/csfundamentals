import math

class Heap:
    def __init__(self, items=[]):
        self.items = items
        if self.items != []:
            self.printHeap()
            for i in range(int(math.floor(len(self.items)/2)), -1, -1):
                self.bubbleDown(i)

    def insert(self, value):
        self.items.append(value)
        self.bubbleUp(len(self.items) - 1)

    def bubbleUp(self, indx):
        if self.items[indx] <= self.items[self.parent(indx)] or indx == 0:
            return
        self.swap(indx, self.parent(indx))
        self.bubbleUp(self.parent(indx))

    def deleteMax(self):
        self.swap(0, len(self.items) - 1)
        val = self.items.pop()
        self.bubbleDown(0)
        return val
        
    def bubbleDown(self, i):
        end = len(self.items)
        left = self.leftChild(i)
        right = self.rightChild(i)
        largest = i

        if left < end and self.items[left] > self.items[largest]:
            largest = left
        if right < end and self.items[right] > self.items[largest]:
            largest = right

        if largest != i:
            print("swapping " + str(i) + " and " + str(largest))
            self.swap(i, largest)
            self.bubbleDown(largest)

    def leftChild(self, i):
        left = 2 * i + 1
        return left

    def rightChild(self, i):
        right = 2 * i + 2
        return right

    def parent(self, i):
        return int(math.floor((i - 1) / 2))

    def swap(self, a, b):
        tmp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = tmp
    
    def printHeap(self):
        s = ""
        for x in self.items:
            s = s + str(x) + ", "
        print(s)

def mergeLists(listA, listB):
    h = Heap()
    while listA != [] or listB != []:
        if listA != []:
            h.insert(listA.pop())
        if listB != []:
            h.insert(listB.pop())
    h.printHeap()
    result = []
    while h.items != []:
        result.append(h.deleteMax())
    print result

def almostSorted(lst, k):
    h = Heap()
    result = []
    for i in range(0, k + 1):
        h.insert(lst.pop())
    while lst != []:
        h.insert(lst.pop())
        result.append(h.deleteMax())
    while h.items != []:
        result.append(h.deleteMax())
    print result

def printKthSmallest(lst, k):
    h = Heap()
    print lst
    for x in range(0,k):
        h.insert(lst.pop())
    while lst != []:
        h.insert(lst.pop())
        print h.deleteMax()
        h.printHeap()

h = Heap()
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(7)
h.insert(4)
h.printHeap()
print(h.deleteMax())
h.printHeap()
print(h.deleteMax())
h.printHeap()
print(h.deleteMax())
h.printHeap()
print(h.deleteMax())
h.printHeap()
print(h.deleteMax())
h.printHeap()

h2 = Heap([1,2,3,4,6,7,10])
h2.printHeap()

mergeLists([1,3,5,7,9], [2,4,6])
#almostSorted([8, 5, 4, 6, 2, -1, 3], 2)
almostSorted([3, -1, 2, 6, 4, 5, 8], 2)
printKthSmallest([1,8,5,0,3,7,6,2,4], 3)
