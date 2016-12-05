class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.isEnd = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode(-1)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.addWordPart(self.root,word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchWordPart(self.root,word)
        
    def searchWordPart(self,root,part):
        if len(part) == 0:
            return root.isEnd
        if part[0] == '.':
            return any(self.searchWordPart(r,part[1:]) for r in root.children.values())
        if part[0] not in root.children.keys():
            return False
        return self.searchWordPart(root.children[part[0]], part[1:])
        
    def addWordPart(self,root,part):
        if part[0] not in root.children.keys():
            root.children[part[0]] = TrieNode(part[0])
        if len(part) > 1:
            self.addWordPart(root.children[part[0]], part[1:])
        else:
            root.children[part[0]].isEnd = True

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")