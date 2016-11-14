# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
            
        helper = ListNode(0)
        curr = head
        pre = helper
        next = None
        
        while curr is not None:
            next = curr.next
            
            while pre.next is not None and pre.next.val < curr.val:
                pre = pre.next
                
            curr.next = pre.next
            pre.next = curr
            pre = helper
            curr = next
            
        return helper.next