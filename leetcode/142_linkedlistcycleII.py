# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head.next
        
        cycle = False
        
        while fast.next is not None and fast.next.next is not None:
            if fast == slow:
                cycle = True
                break
            fast = fast.next.next
            slow = slow.next
            
        if cycle == False: 
            return None
            
        count = 1
        fast = fast.next
        while fast is not slow:
            fast = fast.next
            count += 1
           
        print(count)
        fast = head
        slow = head
        for i in range(count):
            fast = fast.next
        
        while fast is not slow:
            fast = fast.next
            slow = slow.next
            
        return fast