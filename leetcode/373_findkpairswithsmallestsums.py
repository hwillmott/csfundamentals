class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        queue = []
        def push(i,j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i]+nums2[j], i, j])
        push(0,0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i],nums2[j]])
            push(i,j+1)
            if j == 0:
                push(i+1,j)
        return pairs
        