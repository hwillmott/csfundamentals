class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        letters = list(pattern)
        d = dict()
        if len(words) != len(letters):
            return False
        for i in range(len(letters)):
            word = words[i]
            letter = letters[i]
            if letter in d:
                if d[letter] != word:
                    return False
            elif word in d.values():
                return False
            else:
                d[letter] = word
        return True