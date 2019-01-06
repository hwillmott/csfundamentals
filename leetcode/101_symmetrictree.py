# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compare(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False
        
        outer = self.compare(p.left, q.right)
        inner = self.compare(p.right, q.left)
        return outer and inner
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return self.compare(root.left, root.right)
