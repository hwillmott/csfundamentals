class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items = [item] +  self.items

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def print(self):
        print(self.items)

myQueue = Queue()
myQueue.enqueue(2)
myQueue.enqueue(4)
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
