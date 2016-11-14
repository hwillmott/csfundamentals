class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        maxn = 0
        currstr = ""
        
        for ch in s:
            if ch in currstr:
                currstr = currstr[currstr.find(ch)+1:] + ch
            else:
                currstr = currstr + ch
                if len(currstr) > maxn:
                    maxn = len(currstr)
                   
        return maxn