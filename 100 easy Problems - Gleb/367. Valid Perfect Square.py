class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num < 2:
            return True

        l, r = 0, num // 2

        while l <= r:
            m = (l + r) // 2

            sqr = m * m

            if sqr > num:
                r = m - 1
            elif sqr < num:
                l = m + 1
            else:
                return True
        
        return False

