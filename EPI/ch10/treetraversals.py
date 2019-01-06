class TNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Tree:
    def __init__(self, root=None):
        self.root = root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value + " ")
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.value + " ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value + " ")

def balanceCheck(root, depth):
    if root is None:
        return depth
    l = balanceCheck(root.left, depth + 1)
    r = balanceCheck(root.right, depth + 1)
    print(root.value + " (" + str(l) + ", " + str(r) + ")")
    if l == -1 or r == -1 or abs(l-r) > 1:
        return -1
    return max(l, r)
        
def isSymmetric(root):
    return checkSymmetry(root.left, root.right)

def checkSymmetry(left, right):
    if left is None and right is None:
        return True
    elif left is not None and right is not None:
        return left.value == right.value and \
            checkSymmetry(left.left, right.right) and \
            checkSymmetry(left.right, right.left)
    return False

def findLCA(root, a, b):
    if root is None:
        return 0
    left = findLCA(root.left, a, b)
    right = findLCA(root.right, a, b)
#    if left == 2:
#        print root.left.value
#        return 0
#    elif right == 2:
#        print root.right.value
#        return 0
#    else:
    sumVals = left + right
    print("sumVals = " + str(sumVals))
    if root.value == a or root.value == b:
        print("found " + str(root.value))
        sumVals += 1
    if sumVals == 2:
        print(root.value)
        return 0
    return sumVals

na = TNode("a")
nb = TNode("b")
nc = TNode("c")
nd = TNode("d")
ne = TNode("e")
nf = TNode("f")
ng = TNode("g")

na.left = nb
na.right = nc

nb.left = nd
nb.right = ne

nc.left = nf
nc.right = ng

t = Tree(na)

#inorder(na)
#preorder(na)
#postorder(na)
#print(balanceCheck(na, 0))
#print(isSymmetric(na))
findLCA(na, "e", "f")
findLCA(na, "f", "g")
findLCA(na, "b", "c")
