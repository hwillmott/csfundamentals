class Solution(object):
    def grayCode(self, n):
        results = []
        results.append(0)
        for i in range(n):
            for j in range(len(results))[::-1]:
                results.append(results[j] | (1 << i))
        return results