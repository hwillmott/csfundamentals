# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def getPath(root, stringsofar, result):
            if root.left is None and root.right is None:
                result.append(stringsofar + str(root.val))
                return
            if root.left is not None:
                getPath(root.left, stringsofar + str(root.val) + "->", result)
            if root.right is not None:
                getPath(root.right, stringsofar + str(root.val) + "->", result)
        result = []
        if root is not None: getPath(root, "", result)
        return result