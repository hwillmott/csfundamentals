# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val <= p.val:
            return self.inorderSuccessor(root.right,p)
        left = self.inorderSuccessor(root.left,p)
        return left if left is not None else root