class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        notval = "23457"
        
        lo = 0
        hi = len(num)-1
        while lo <= hi:
            if num[lo] in notval or num[hi] in notval:
                return False
            if num[lo] != d[num[hi]]:
                return False
            lo += 1
            hi -= 1
        return True