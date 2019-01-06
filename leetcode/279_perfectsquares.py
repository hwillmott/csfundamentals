class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        i = 1
        lst = []
        while i*i <= n: 
            lst.append(i*i)
            i += 1
        toCheck = {n}
        count = 0
        while toCheck:
            count += 1
            temp = set()
            for t in toCheck:
                for i in lst:
                    if t == i: return count
                    if t < i: break
                    temp.add(t-i)
            toCheck = temp
        return count