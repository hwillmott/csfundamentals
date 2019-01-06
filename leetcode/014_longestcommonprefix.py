class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        strs = sorted(strs)
        count = 0
        
        str1 = strs[0]
        str2 = strs[len(strs) - 1]
        maxLen = min(len(str1), len(str2))

        while count < maxLen:
            if str1[count] != str2[count]:
                break
            count += 1
        
        return str1[0:count]