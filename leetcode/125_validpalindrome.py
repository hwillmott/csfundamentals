class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        s = s.translate({ord(c): None for c in string.punctuation})
        s = s.lower()
        s = ''.join(s.split())
        return s == s[::-1]