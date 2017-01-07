class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations, reverse=True)
        h = 0
        for i in range(1,len(citations)+1):
            if citations[i-1] >= i:
                if i == len(citations) or citations[i] <= i:
                    h = max(h,i)
        return h