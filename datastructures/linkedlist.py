class Node:
    def __init__(self, item):
        self.value = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        n = Node(item)
        n.next = self.head
        self.head = n

    def delete(self, item):
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == item:
                break
            prev = curr
            curr = curr.next
        if curr is None:
            return
        if prev is None:
            self.head = curr.next
            return
        prev.next = curr.next

    def deleteNode(self, node):
        if node.next is None:
            node = None
            return
        node.value = node.next.value
        node.next = node.next.next

    def findNode(self, item):
        curr = self.head
        while curr is not None:
            if curr.value == item:
                return curr
            curr = curr.next
        return None

    def print(self):
        curr = self.head
        s = ""
        while curr is not None:
            s += str(curr.value) + "->"
            curr = curr.next
        print(s)


#for i in range(5):
    #ll.insert(i)

#ll.print()

#c = ll.findNode(2)
#ll.deleteNode(c)
#ll.print()

#ll.delete(0)
#ll.print()

#ll.delete(3)
#ll.print()

#ll.delete(4)
#ll.print()

#ll.delete(1)
#ll.print()

