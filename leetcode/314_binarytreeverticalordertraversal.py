# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def verticalOrder(self, root):
        verticals = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                verticals[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [verticals[i] for i in sorted(verticals)]