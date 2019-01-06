# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkValid(root,minimum,maximum):
            if root is None: return True
            if (maximum is not None and root.val >= maximum) or (minimum is not None and root.val <= minimum):
                return False
            return checkValid(root.left, minimum, root.val) and checkValid(root.right, root.val, maximum)
        return checkValid(root,None,None)