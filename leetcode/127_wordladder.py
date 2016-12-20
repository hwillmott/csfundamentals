class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        path = 1
        queue = [beginWord]
        visited = set([beginWord])
        while queue:
            tmp = queue.pop()
            for i in range(len(tmp)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    tmp2 = tmp[:i] + c + tmp[i+1:]
                    if tmp2 == endWord:
                        return path
                    if tmp2 not in visited and tmp2 in wordList:
                        queue = [tmp2] + queue
                        visited.add(tmp2)
            path += 1
        return 0