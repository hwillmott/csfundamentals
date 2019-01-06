# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next is not None and curr.next.next is not None:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            curr.next = second
            curr.next.next = first
            curr = curr.next.next
            
        return dummy.next