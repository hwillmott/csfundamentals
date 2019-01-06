class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        alphabet = [0]*26
        for sc in s:
            alphabet[ord(sc) - ord('a')] += 1
        for tc in t:
            alphabet[ord(tc) - ord('a')] -= 1
        for a in alphabet:
            if a != 0:
                return False
        return True