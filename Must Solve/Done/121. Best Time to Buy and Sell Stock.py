class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] - prices[l] > 0:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        
        return maxProfit
