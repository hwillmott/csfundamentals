# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def goLeft(stack, root):
            curr = root
            while curr is not None:
                stack.append(curr)
                curr = curr.left
        stack = []
        queue = []
        goLeft(stack,root)
        for i in range(k):
            tmp = stack.pop()
            goLeft(stack, tmp.right)
            
        return tmp.val