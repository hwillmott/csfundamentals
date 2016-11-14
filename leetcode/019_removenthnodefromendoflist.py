# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        
        target = ListNode(0)
        target.next = head
        end = target
        mid = target
        
        for i in range(n):
            end = end.next
        
        print(end.val)
        while end.next != None:
            print(str(end.val) + " " + str(mid.val))
            end = end.next
            mid = mid.next
            
        mid.next = mid.next.next
        
        return target.next