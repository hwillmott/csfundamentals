# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDepth(self, root, depth):
        if root is None: 
            return depth
        leftD = self.getDepth(root.left, depth+1)
        rightD = self.getDepth(root.right, depth+1)
        return max(leftD, rightD)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root, 0)