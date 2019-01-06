class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if word is None or abbr is None or len(word) == 0 or len(abbr) == 0: return False
        wPos = 0
        aPos = 0
        while aPos < len(abbr) and wPos < len(word):
            if word[wPos] == abbr[aPos]:
                wPos += 1
                aPos += 1
                continue
            if not abbr[aPos].isdigit(): return False
            start = aPos
            if abbr[start] == "0": return False
            while aPos < len(abbr) and abbr[aPos].isdigit():
                aPos += 1
            num = int(abbr[start:aPos])
            wPos += num
 
        return True if aPos == len(abbr) and wPos == len(word) else False