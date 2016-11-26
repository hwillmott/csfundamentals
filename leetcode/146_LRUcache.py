class LLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.numitems = 0
        self.head = None
        self.tail = None
        self.cache = dict()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.movetohead(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        n = self.cache.get(key)
        if n is None:
            node = LLNode(value)
            if self.numitems == self.capacity:
                self.deletefromcache(self.tail)
                self.deletetail()
            self.addtocache(key, node)
            self.movetohead(node)
        else:
            self.movetohead(n)
        
        
    def movetohead(self, node):
        p = node.prev
        n = node.next
        
        if p is not None:
            p.next = n
        if n is not None:
            n.prev = p
        
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        
    def deletetail(self):
        p = self.tail.prev
        
        if p is not None:
            p.next = None
            self.tail = p
        else:
            self.tail = None
            self.head = None
    
    def addtocache(self, key, node):
        self.cache[key] = node
        self.numitems += 1
    
    def deletefromcache(self, node):
        for k,v in self.cache.items():
            if v == node:
                del self.cache[k]
                break
        self.numitems -= 1