class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  
        s.sort()  

        count = 0
        l, r = 0, 0

        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                count += 1
                l += 1
            r += 1

        return count
