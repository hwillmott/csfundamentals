# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        queue = []
        heapq.heappush(queue, intervals[0].end)
        for i in range(1, len(intervals)):
            if queue[0] <= intervals[i].start:
                heapq.heapreplace(queue, intervals[i].end)
            else:
                return False
        return True
            