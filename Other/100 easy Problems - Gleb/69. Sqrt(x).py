class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l, r = 0, x//2

        while l <= r:
            m = (l + r) // 2
            sq = m * m

            if sq == x:
                return m
            elif sq < x:
                l = m + 1
            else:
                r = m - 1

        return r




class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 1, x
        
        while l<=r:
            m = (l + r) // 2
            sqr = m * m

            if sqr == x:
                return m

            if sqr < x and (m+1)*(m+1) > x:
                return m

            if sqr > x and (m+1)*(m+1) > x:
                r = m 
            else:
                l = m

        return -1