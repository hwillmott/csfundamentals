class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        d = dict()
        res = dict()
        for i in range(len(s)-9):
            tmpstr = s[i:i+10]
            if tmpstr in d and tmpstr not in res:
                res[tmpstr] = 1
            else:
                d[tmpstr] = 1
        return res.keys()