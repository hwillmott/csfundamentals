# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr1 = headA
        curr2 = headB
        count1 = 0
        count2 = 0
        if curr1 is None or curr2 is None:
            return None
        while curr1.next is not None:
            curr1 = curr1.next
            count1 = count1 + 1
        while curr2.next is not None:
            curr2 = curr2.next
            count2 = count2 + 1
        if curr1 != curr2:
            return None
        curr1 = headA
        curr2 = headB
        if count1 > count2:
            diff = count1 - count2
            for i in range(diff):
                curr1 = curr1.next
        elif count2 > count1:
            diff = count2 - count1
            for i in range(diff):
                curr2 = curr2.next
        while curr1 is not curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1