import random

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, value):
        if self.value > value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = Node(value, self)
        elif self.value < value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = Node(value, self)


    def delete(self, value):
        if self.value > value:
            if self.left is not None:
                self.left.delete(value)
        elif self.value < value:
            if self.right is not None:
                self.right.delete(value)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.findMin()
                print("setting value from " + str(value) + " to " + str(self.value))
                self.right.delete(self.value)
            elif self.left is not None:
                self.replaceNodeForParent(self.left)
            elif self.right is not None:
                self.replaceNodeForParent(self.right)
            else:
                self.replaceNodeForParent(None)

    def replaceNodeForParent(self, node):
        if self.parent is not None:
            if self == self.parent.left:
                self.parent.left = node
            else:
                self.parent.right = node
        else:
            print("self.parent is None")
        if node is not None:
            node.parent = self.parent


    def findMin(self):
        if self.left is None:
            return self.value
        else:
            return self.left.findMin()

    def search(self, value):
        if self.value == value:
            print("found " + str(value))
            return
        elif value < self.value:
            if self.left is None:
                print("didn't find " + str(value))
                return
            self.left.search(value)
        else:
            if self.right is None:
                print("didn't find " + str(value))
                return
            self.right.search(value)

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def delete(self, value):
        if self.root is None:
            return
        elif self.root.value == value:
            tmp = Node(0)
            tmp.left = self.root
            self.root.parent = tmp
            self.root.delete(value)
            self.root = tmp.left
        else:
            self.root.delete(value)

def findKLargest(root, array, k):
    if len(array) == k:
        return
    if root is not None:
        findKLargest(root.right, array, k)
        array.append(root.value)
        findKLargest(root.left, array, k)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print str(root.value)
        inorder(root.right)

def checkForBST(root):
    isBST = True
    if root.left is not None:
        if root.left.value > root.value:
            return False
        else:
            isBST = checkForBST(root.left)
    if root.right is not None:
        if root.right.value < root.value:
            return False
        else:
            isBST = checkForBST(root.right)
    return isBST

def findLCA(root, s, b):
    if root.value == s or root.value == b:
        return root
    elif root.value > s and root.value < b:
        return root
    elif root.value > s and root.value > b:
        return findLCA(root.left, s, b)
    else:
        return findLCA(root.right, s, b)

t = BST()
ints = [7,4,8,2,3,0,9,6,1,5]
for i in ints:
    t.insert(i)
inorder(t.root)

arr = []
findKLargest(t.root, arr, 3)
print arr

print(str(findLCA(t.root, 3, 5).value))

print(str(findLCA(t.root, 5, 6).value))

t.root.search(3)
t.root.search(10)

#for i in ints:
#    print("deleting " + str(i))
#    t.delete(i)
#    inorder(t.root)

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)

nodeA.left = nodeB
nodeA.right = nodeC

print checkForBST(nodeA)
