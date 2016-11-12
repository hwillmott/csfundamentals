from linkedlist import Node
import random

def mergesort(head):
    if head.next is None:
        return head
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    l2 = slow.next
    slow.next = None
    l1 = head
    l1 = mergesort(l1)
    l2 = mergesort(l2)

    final = mergelists(l1,l2)
    return final

def mergelists(l1,l2):
    dummy = Node(-1)
    l3 = dummy
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            l3.next = l1
            l1 = l1.next
            l3 = l3.next
        else:
            l3.next = l2
            l2 = l2.next
            l3 = l3.next

    if l1 is not None:
        l3.next = l1
    if l2 is not None:
        l3.next = l2
    return dummy.next

def printlist(head):
    curr = head
    while curr is not None:
        print(curr.value, end="->")
        curr = curr.next
    print()

n = Node(100)
curr = n

for i in range(10):
    curr.next = Node(random.randint(0,100))
    curr = curr.next

printlist(n)

f = mergesort(n)

printlist(f)
