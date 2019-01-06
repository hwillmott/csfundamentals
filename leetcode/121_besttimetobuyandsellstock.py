class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minn = prices[0]
        maxx = 0
        
        for i in range(len(prices)):
            minn = min(minn, prices[i])
            maxx = max(maxx, prices[i] - minn)
        return maxx