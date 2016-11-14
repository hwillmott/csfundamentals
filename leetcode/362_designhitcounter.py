class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0 for i in range(300)]
        self.lasttime = [0 for i in range(300)]
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        m = timestamp % 300
        if timestamp != self.lasttime[m]:
            self.hits[m] = 1
            self.lasttime[m] = timestamp
        else:
            self.hits[m] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        h = 0
        for i in range(300):
            if timestamp - self.lasttime[i] <300:
                h += self.hits[i]
        return h
                


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)