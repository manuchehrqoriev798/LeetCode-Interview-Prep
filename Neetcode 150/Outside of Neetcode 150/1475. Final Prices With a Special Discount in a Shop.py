class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) < 2:
            return prices
            
        res = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            res.append(prices[i] - discount)
        return res



class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i] and j>i:
                    prices[i]-=prices[j]
                    break

        return prices

        