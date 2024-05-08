# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr1 = l1
        curr2 = l2
        
        result = ListNode(0)
        curr3 = result
        s = 0
        while curr1 is not None or curr2 is not None:
            s /= 10
            if curr1 is not None:
                s += curr1.val
                curr1 = curr1.next
            if curr2 is not None:
                s += curr2.val
                curr2 = curr2.next
            curr3.next = ListNode(s%10)
            curr3 = curr3.next
        if s/10 == 1:
            curr3.next = ListNode(1)
        return result.next
