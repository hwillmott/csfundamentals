class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == m:
            return
        write = len(nums1)-1
        read1 = m-1
        read2 = n-1
        while read1 >= 0 or read2 >= 0:
            if read1 >= 0 and read2 >= 0:
                if nums1[read1] > nums2[read2]:
                    nums1[write] = nums1[read1]
                    read1 -= 1
                else:
                    nums1[write] = nums2[read2]
                    read2 -= 1
            elif read1 >= 0:
                nums1[write] = nums1[read1]
                read1 -= 1
            else:
                nums1[write] = nums2[read2]
                read2 -= 1
            write -= 1
