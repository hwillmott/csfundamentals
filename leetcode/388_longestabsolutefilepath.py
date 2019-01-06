class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxLen = 0
        pathLen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line)-len(name)
            if '.' in name:
                maxLen = max(maxLen, pathLen[depth] + len(name))
            else:
                pathLen[depth+1] = pathLen[depth] + len(name) + 1
        return maxLen