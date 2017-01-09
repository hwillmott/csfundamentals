class TrieNode(object):
    def __init__(self, value):
        self.val = value
        self.children = dict()
        
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        def backtrack(wordsSoFar, wordsNeeded, results):
            if len(wordsSoFar) == wordsNeeded:
                results.append(wordsSoFar)
                return
            prefix = ""
            l = len(wordsSoFar)
            for i in range(l):
                prefix += wordsSoFar[i][l]
            node = self.findNode(prefix, self.trie)
            if node is None: return
            children = []
            self.findAllChildren(prefix, node, children)
            for c in children:
                backtrack(wordsSoFar + [c], wordsNeeded, results)
        
        if len(words) == 0:
            return []
        self.trie = TrieNode(0)
        for w in words:
           self.insert(w, self.trie)
        results = []
        backtrack([], len(words[0]), results)
        return results
            
    def findAllChildren(self, prefix, node, results):
        if len(node.children) == 0:
            results.append(prefix)
            return
        for c,n in node.children.items():
            self.findAllChildren(prefix + c, n, results)
        
            
    def findNode(self, prefix, node):
        if len(prefix) == 0:
            return node
        if node is None or prefix[0] not in node.children:
            return None
        return self.findNode(prefix[1:], node.children[prefix[0]])
        
        
    def insert(self, word, root):
        if len(word) == 0:
            return
        if word[0] not in root.children:
            root.children[word[0]] = TrieNode(word[0])
        self.insert(word[1:],root.children[word[0]])
        
        
        
        
        
        
        
        
        
        