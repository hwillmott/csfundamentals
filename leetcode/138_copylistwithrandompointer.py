class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        d = dict()
        d[None] = None
        curr = head
        while curr:
            d[curr] = RandomListNode(curr.label)
            curr = curr.next
        curr = head
        while curr:
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]
            curr = curr.next
        return d[head]