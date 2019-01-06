# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def dfs(root, closest, target):
            if root is None:
                return closest
            if root.val == target: 
                return root.val
            if abs(closest-target) > abs(root.val-target):
                closest = root.val
            cl = dfs(root.left, closest, target)
            cr = dfs(root.right, closest, target)
            if abs(closest-target) > abs(cl-target):
                closest = cl
            if abs(closest-target) > abs(cr-target):
                closest = cr
            return closest
            
        if root is None: return None
        return dfs(root, root.val, target)
            
        