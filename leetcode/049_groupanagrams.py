class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        return d.values()