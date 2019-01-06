# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        toChange = dummy
        curr = dummy
        while curr.next is not None:
            curr = curr.next
            if curr.val < 9:
                toChange = curr
        if curr.val < 9:
            curr.val += 1
        else:
            toChange.val += 1
            toChange = toChange.next
            while toChange is not None:
                toChange.val = 0
                toChange = toChange.next
                
        if dummy.val == 0:
            return dummy.next
        return dummy