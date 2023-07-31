class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        indlo = 0
        indhi = 1
        maxprofit = 0
        while indhi < len(prices):
            tempprofit = prices[indhi] - prices[indlo]
            if prices[indlo] < prices[indhi]:
                maxprofit = max(tempprofit, maxprofit)
            else:
                indlo = indhi
            indhi += 1
        return maxprofit
