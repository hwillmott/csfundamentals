# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
            
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        
        while curr is not None and curr.next is not None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return dummy.next