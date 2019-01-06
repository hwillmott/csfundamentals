class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findLCA(nodeA, nodeB):
    currA = nodeA
    currB = nodeB
    d = dict()
    print("in LCA")
    while currA != None or currB != None:
        if currA != None:
            print("currA: " + str(currA.value))
            if currA.value in d:
                return currA.value
            else:
                d[currA.value] = 1
            currA = currA.parent
        if currB != None:
            print("currB: " + str(currB.value))
            if currB.value in d:
                return currB.value
            else:
                d[currB.value] = 1
            currB = currB.parent
    return None

nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeG = Node('g')

nodeA.left = nodeB
nodeA.right = nodeC

nodeB.left = nodeD
nodeB.right = nodeE

nodeB.parent = nodeA
nodeD.parent = nodeB
nodeE.parent = nodeB

nodeC.left = nodeF
nodeC.right = nodeG

nodeC.parent = nodeA
nodeF.parent = nodeC
nodeG.parent = nodeC

print findLCA(nodeC, nodeG)
print findLCA(nodeB, nodeF)
print findLCA(nodeD, nodeE)
