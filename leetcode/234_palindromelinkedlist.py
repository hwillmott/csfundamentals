# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverseList(slow.next)
        slow = slow.next
        while slow is not None:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
        
        
    def reverseList(self, node):
        prev = None
        curr = node
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev