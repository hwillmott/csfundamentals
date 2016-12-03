class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 or l2 == 0:
            return []
        d = dict()
        res = dict()
        for i in range(l1):
            if nums1[i] not in d:
                d[nums1[i]] = 1
        for i in range(l2):
            if nums2[i] in d and nums2[i] not in res:
                res[nums2[i]] = 1
        return res.keys()