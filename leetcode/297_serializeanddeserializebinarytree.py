# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node,nodes):
            if node:
                nodes.append(str(node.val))
                preorder(node.left,nodes)
                preorder(node.right,nodes)
            else:
                nodes.append("#")
        nodes = []
        preorder(root,nodes)
        return ' '.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        vals = iter(data.split())
        return preorder()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))