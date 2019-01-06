# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        return self.makeBST(head, None)
        
    def makeBST(self, head, tail):
        if head == tail:
            return None
        fast = head
        slow = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        middle = TreeNode(slow.val)
        middle.left = self.makeBST(head, slow)
        middle.right = self.makeBST(slow.next, tail)
        return middle