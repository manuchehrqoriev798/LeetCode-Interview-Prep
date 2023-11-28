class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l < r:
            k = (l + r) // 2
            total_hours = 0

            for pile in piles:
                total_hours += ceil(pile / k)
            
            if total_hours <= h:
                res = min(res, k)
                r = k 
            else:
                l = k + 1
        
        return res



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / k)
                if total_hours > h:
                    break

            if total_hours <= h:
                right = k
            else:
                left = k + 1

        return right