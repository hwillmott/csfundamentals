class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s[::-1]
        s2 = s1.split()
        for i in range(len(s2)):
            s2[i] = s2[i][::-1]
            
        return "" + " ".join(s2)