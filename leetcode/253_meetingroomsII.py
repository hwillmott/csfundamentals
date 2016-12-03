# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda i: i.start)
        heap = []
        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heappop(heap)
                heapq.heappush(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)
            