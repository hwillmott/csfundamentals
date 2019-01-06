# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
        
        
        
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        prev = head
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        l1 = self.mergeSort(head)
        l2 = self.mergeSort(slow)
        
        return self.mergeLists(l1, l2)
        
        
    def mergeLists(self, l1, l2):
        dummy = ListNode(0)
        l3 = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
                
        if l1 is not None:
            l3.next = l1
        elif l2 is not None:
            l3.next = l2
        return dummy.next
        
        
    def printList(self, head):
        strn = ""
        while head is not None:
            strn += str(head.val) + ", "
            head = head.next
        print(strn)