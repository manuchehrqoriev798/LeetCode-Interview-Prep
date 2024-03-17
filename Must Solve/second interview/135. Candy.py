class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        
        for i, rating in enumerate(ratings[:-1]):
            if rating < ratings[i+1]:
                candies[i+1] = max(candies[i]+1, candies[i+1])
                
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                candies[i] = max(candies[i+1]+1, candies[i])
                    
        return sum(candies)