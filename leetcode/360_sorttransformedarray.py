class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        calc = [a*x*x + b*x + c for x in nums]
        res = [0 for x in nums]
        if a >= 0:
            writeIdx = len(nums)-1
        else:
            writeIdx = 0
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            if a >= 0:
                if calc[lo] >= calc[hi]:
                    res[writeIdx] = calc[lo]
                    lo += 1
                else:
                    res[writeIdx] = calc[hi]
                    hi -= 1
                writeIdx -= 1
            else:
                if calc[lo] <= calc[hi]:
                    res[writeIdx] = calc[lo]
                    lo += 1
                else:
                    res[writeIdx] = calc[hi]
                    hi -= 1
                writeIdx += 1
        return res