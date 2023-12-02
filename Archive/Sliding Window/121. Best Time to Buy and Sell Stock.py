class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left=buy right=sell
        max_profit = 0 
        

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit, profit)
            else: # non profitable, then change left pointer all the way to the right and keep calculating
                l = r
            r += 1

        return max_profit


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                r += 1
        
        return max_profit




# Another implementation of the same problem using a different approach.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of the minimum and maximum prices,
        # as well as the maximum profit.
        mini = prices[0]
        maxi = prices[0]
        prof = 0

        # Iterate through the prices.
        for i in prices:
            # Check if the current price is lower than the minimum price.
            if i < mini:
                # Update the maximum profit if the difference between maximum and minimum is greater.
                prof = max(maxi - mini, prof)
                # Update the minimum and maximum prices to the current price.
                mini = i
                maxi = i
            # Check if the current price is higher than the maximum price.
            elif i > maxi:
                # Update the maximum price to the current price.
                maxi = i
        
        # Return the maximum profit, considering the last segment of prices.
        return max(maxi - mini, prof)






class Solution:
    def maxProfit(self, prices) -> int:
        # Check if the list of prices has less than 2 elements
        if len(prices) < 2:
            # If so, there's no opportunity to make a profit, return 0
            return 0

        # Initialize variables to track maximum profit and minimum price
        maxProfit = 0
        minPrice = prices[0]

        # Iterate through prices starting from the second element
        for price in prices[1:]:
            # Update the maximum profit by taking the maximum of the current maxProfit
            # and the difference between the current price and the minimum price so far
            maxProfit = max(maxProfit, price - minPrice)
            
            # Update the minimum price to be the minimum of the current price and the
            # minimum price so far
            minPrice = min(price, minPrice)

        # Return the maximum profit
        return maxProfit


