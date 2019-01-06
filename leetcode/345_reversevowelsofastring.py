class Solution(object):
    def isvowel(self,c):
        return True if c.lower() in 'aeiou' else False
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            while start < end and not self.isvowel(s[start]):
                start += 1
            while end > start and not self.isvowel(s[end]):
                end -= 1
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)