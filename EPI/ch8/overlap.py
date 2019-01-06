from linkedlist import LinkedList

def findOverlap(l1, l2):
    iter1 = l1.head
    iter2 = l2.head
    count1 = 0
    count2 = 0
    while iter1.nxt:
        count1 += 1
        iter1 = iter1.nxt
    while iter2.nxt:
        count2 += 1
        iter2 = iter2.nxt
    if iter1 == iter2:
        print("found an overlap!!!")
        if count1 > count2:
            count1 = count1 - count2
            iter1 = l1.head
            iter2 = l2.head
        else:
            count1 = count2 - count1
            iter1 = l2.head
            iter2 = l1.head
        for i in range(0,count1):
            iter1 = iter1.nxt
        while iter1 != iter2:
            iter1 = iter1.nxt
            iter2 = iter2.nxt
        print(iter1.value)
        return iter1
    return None

l1 = LinkedList()
l1.insertMultiple([1,2,3])
l2 = LinkedList()
l2.insertMultiple([4,5,6,7,8,9,10,11,12])
ptr = l2.head
for i in range(4):
    ptr = ptr.nxt
l1.tail.nxt = ptr
findOverlap(l1,l2)
