class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for l in jewels:
            for r in stones:
                if l == r:
                    count += 1
        
        return count