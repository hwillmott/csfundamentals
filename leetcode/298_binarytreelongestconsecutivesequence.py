# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(count,last,node):
            if node is None: return count
            if node.val == last + 1:
                count += 1
            else:
                count = 1
            left = dfs(count,node.val,node.left)
            right = dfs(count,node.val,node.right)
            return max(max(left,right),count)
            
        if root is None:
            return 0
        else:
            return max(dfs(1, root.val, root.left), dfs(1, root.val, root.right))