class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        len_prices = len(prices)
        for a in range(len_prices-1):
            for b in range(a+1, len_prices):
                if prices[a] >= prices[b]:
                    prices[a] = prices[a] - prices[b]
                    break
        return(prices)
