class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        if s is None or len(s) == 0: return results
        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                results.append(s[:i] + "--" + s[i+2:])
        return results