# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        def getDepth(root, depth):
            if root is None:
                return depth
            l = getDepth(root.left, depth+1)
            r = getDepth(root.right, depth+1)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l,r)
        return getDepth(root, 1) != -1