from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PriorityQueue()
        dummy = ListNode(0)
        curr = dummy
        for l in lists:
            if l:
                pq.put((l.val, l))
        while pq.qsize() > 0:
            curr.next = pq.get()[1]
            curr = curr.next
            if curr.next:
                pq.put((curr.next.val, curr.next))
        return dummy.next