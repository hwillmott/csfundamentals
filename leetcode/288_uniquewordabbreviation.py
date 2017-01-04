class ValidWordAbbr(object):
            
    def getAbbrev(self, word):
        num = len(word) - 2
        if num > 0:
            return word[0] + str(num) + word[-1]
        return word
    
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        d = dict()
        for w in dictionary:
            a = self.getAbbrev(w)
            if a in d:
                d[a].add(w)
            else:
                d[a] = set()
                d[a].add(w)
        self.d = d

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        a = self.getAbbrev(word)
        if a not in self.d or (a in self.d and len(self.d[a]) == 1 and word in self.d[a]): return True
        else: return False



# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")