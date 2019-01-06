class Solution(object):
    def firstUniqChar(self, s):
        letters = list("abcdefghijklmnopqrstuvwxyz")
        return reduce(lambda i,j: min(i,j), map(lambda y: s.index(y), filter(lambda x: s.count(x) == 1, letters)))