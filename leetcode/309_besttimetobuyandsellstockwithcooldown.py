class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        buy = [0]*len(prices)
        sell = [0]*len(prices)
        buy[0] = -prices[0]
        buy[1] = max(buy[0], -prices[1])
        
        for i in range(1,len(prices)):
            if i > 1:
                buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
        return sell[-1]