class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = [0]*26
        for c in magazine:
            letters[ord(c)-ord('a')] += 1
        for r in ransomNote:
            letters[ord(r) - ord('a')] -= 1
            if letters[ord(r) - ord('a')] < 0: return False
        return True