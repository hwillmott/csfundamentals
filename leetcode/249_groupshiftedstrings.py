class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if strings is None or len(strings) == 0: return []
        d = dict()
        for s in strings:
            first = ord(s[0])-ord('a')
            diffs = "0"
            for i in range(1,len(s)):
                tmp = ord(s[i]) - ord('a') - first
                if tmp < 0: tmp += 26
                diffs += "*" + str(tmp)
            if diffs in d:
                d[diffs].append(s)
            else:
                d[diffs] = [s]
        return d.values()