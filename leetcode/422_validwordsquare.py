class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if words is None or len(words) == 0: return True
        
        n = len(words)
        for i in range(n):
            for j in range(len(words[i])):
                if j >= n or len(words[j]) <= i or words[i][j] != words[j][i]:
                    return False
        return True