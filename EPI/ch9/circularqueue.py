class CircularQueue:
    def __init__(self):
        self.maxSize = 10
        self.items = [None] * self.maxSize
        self.count = 0
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.count == 0:
            self.items[self.head] = item
            self.count = 1
        else:
            var = (self.head + 1) % self.maxSize
            if var == self.tail:
                print("resizing")
                self.resize()
                self.enqueue(item)
            else:
                print("enqueue " + str(self.head) + " " + str(self.tail) + " " + str(item))
                self.head = var
                self.items[self.head] = item
                self.count += 1

    def dequeue(self):
        if self.count == 0:
            return None
        elif self.count == 1:
            self.count = 0
            return self.items[self.tail]
        else:
            var = self.items[self.tail]
            print("dequeue " + str(self.head) + " " + str(self.tail) + " " + str(var))
            self.tail = (self.tail + 1) % self.maxSize
            self.count -= 1
            return var

    def resize(self):
        newMax = self.maxSize * 2
        newArray = [None] * newMax
        count = 0
        while not self.isEmpty():
            newArray[count] = self.dequeue()
            count += 1
        self.maxSize = newMax
        self.items = newArray
        self.tail = 0
        self.head = count - 1
        self.count = count

    def printQueue(self):
        curr = self.tail
        result = "["
        while curr != self.head:
            result += str(self.items[curr]) + ", "
            curr = (curr + 1) % self.maxSize
        result += str(self.items[curr])
        result += "]"
        print result

s = CircularQueue()
s.enqueue('a')
s.enqueue('b')
s.enqueue('c')
s.enqueue('d')
s.enqueue('e')
s.enqueue('f')
s.enqueue('g')
s.enqueue('h')
s.enqueue('i')
s.enqueue('j')
s.enqueue('k')
s.enqueue('l')
s.enqueue('m')
s.printQueue()
