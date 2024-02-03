class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res



class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length = len(candies)
        candy_max = max(candies)
        greatest = [False] * length
        for i in range(length):
            if candies[i] + extraCandies >= candy_max:
                greatest[i] = True 
        return greatest
        