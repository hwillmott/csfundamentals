from linkedlist import LinkedList

def findCycle(head):
    fast = head
    slow = head
    cycleLength = 0
    while fast and fast.nxt and fast.nxt.nxt:
        slow = slow.nxt
        fast = fast.nxt.nxt
        if fast == slow:
            while True:
                cycleLength += 1
                fast = fast.nxt
                if fast == slow:
                    break
            print(cycleLength)
            fast = head
            slow = head
            for i in range(0, cycleLength):
                fast = fast.nxt
            while fast != slow:
                fast = fast.nxt
                slow = slow.nxt
            print(slow.value)
            return slow
    return None

lst = LinkedList()
lst.insertMultiple([1,2,3,4,5,6,7,8,9])
lst.prnt()
ptr = lst.head
for i in range(3):
    ptr = ptr.nxt
lst.tail.nxt = ptr
findCycle(lst.head)
