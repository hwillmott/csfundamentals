from linkedlist import LinkedList

def mergeLists(listA, listB):
    listR = LinkedList()
    ptrA = listA.head
    ptrB = listB.head

    while (ptrA != None) or (ptrB != None):
        if ptrA == None:
            listR.append(ptrB)
            listR.tail = listB.tail
            ptrB = listB.tail.nxt
        elif ptrB == None:
            listR.append(ptrA)
            listR.tail = listA.tail
            ptrA = listA.tail.nxt
        else: 
            if ptrA.value < ptrB.value:
                listR.append(ptrA)
                ptrA = ptrA.nxt
            else:
                listR.append(ptrB)
                ptrB = ptrB.nxt
    listR.prnt()

def reverseRecursively(ptr):
    if (ptr == None) or (ptr.nxt == None):
        return ptr
    new_ptr = reverseRecursively(ptr.nxt)
    ptr.nxt.nxt = ptr
    ptr.nxt = None
    return new_ptr

def reverseIteratively(ptr):
    curr = ptr
    prev = None
    while curr:
        nxt = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = nxt
    return prev

def reverseSublist(ptr, i, j):
    x = 0
    curr = ptr
    prev = ptr
    iptr = ptr
    while x < i:
        prev = iptr
        iptr = iptr.nxt
        x += 1
    print(iptr.value)
    curr = iptr
    for x in range(i, j):
        tmp = curr.nxt
        curr.nxt = tmp.nxt
        tmp.nxt = prev.nxt
        prev.nxt = tmp

aList = LinkedList()
aList.insertMultiple([1, 3, 5, 7, 8, 9])
aList.prnt()
bList = LinkedList()
bList.insertMultiple([2, 2, 3, 4, 6, 7, 10])
bList.prnt()
mergeLists(aList, bList)

print("_________________")
cList = LinkedList()
cList.prnt()
dList = LinkedList()
dList.insertMultiple([1,2,3])
dList.prnt()
mergeLists(cList,dList)


print("_________________")
eList= LinkedList()
eList.insertMultiple([2,5,1,3,6,7,8])
eList.prnt()
eList.head = reverseRecursively(eList.head)
eList.prnt()

print("__________________")
fList = LinkedList()
fList.insertMultiple([1,2,3,4,5])
fList.prnt()
fList.head = reverseIteratively(fList.head)
fList.prnt()

print("_________________")
gList = LinkedList()
gList.insertMultiple([1,2,3,4,5,6,7,8,9])
gList.prnt()
reverseSublist(gList.head, 2, 6)
gList.prnt()
