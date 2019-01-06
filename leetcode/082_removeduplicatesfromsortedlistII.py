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
        prev = dummy
        curr = head
        
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                tmp = curr.next
                while tmp is not None and tmp.val == curr.val:
                    tmp = tmp.next
                prev.next = tmp
                curr = tmp
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next